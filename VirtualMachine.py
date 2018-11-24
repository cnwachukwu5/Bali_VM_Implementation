import sys
import operator
import traceback
from ByteCodeUtility import ByteCodeUtility

class Stack(object):
    def __init__(self, sp = 0):
        self.stack = []
        self._sp = sp
    def push(self, value):
        self.stack.append(value)
        self._sp = len(self.stack)
    def pop(self):
        value = self.stack.pop()
        self._sp = len(self.stack)
        return value
    def print(self):
        print("<< STACK {}>> ".format(len(self.stack)), end='')
        for v in self.stack:
            print(v, end=':')
        print()
    def __setitem__(self, key, value):
        self.stack[key] = value
    def __getitem__(self, key):
        return self.stack[key]
    def get_sp(self):
        return self._sp
    def set_sp(self, value):
        self._sp = value
    sp = property(get_sp, set_sp)

class EndOfProgram(Exception):
    pass

class BaliVirtualMachine(object):
    def __init__(self, bytecode):
        self.bytecode = bytecode
        self.bytecode_utility = ByteCodeUtility(self.bytecode)
        self.label_resolved_bytecode = self.bytecode_utility.resolved_bytecode

        self.global_variables = {}
        self.stack = Stack()

        self.pc = 0
        self.bp = 0

    def print(self):
        self.bytecode_utility.print()

    def run(self, debug=False):
        def get_bytecode(pc):
            code_size = len(self.label_resolved_bytecode)
            if (pc < code_size):
                bytecode = self.label_resolved_bytecode[pc]
                res = "{}".format(bytecode.command)
                if bytecode.arg1 is not None:
                    res += " {}".format(bytecode.arg1)
                if bytecode.arg2 is not None:
                    res += "| {}".format(bytecode.arg2)
                return res
            else:
                raise Exception("no next code")

        while True:
            try:
                if debug:
                    oldpc = self.pc
                    bytecode1 = get_bytecode(self.pc)

                result = self.execute(self.label_resolved_bytecode[self.pc])
                if result == 0:
                    self.pc += 1
                else:
                    self.pc = result

                if debug:
                    bytecode2 = get_bytecode(self.pc)
                    print("**DEBUG**: current pc is {} ({}) and next pc is {} ({})".format(oldpc, bytecode1,self.pc, bytecode2))
                    print("sp:({}) bp:({})".format(self.stack.sp, self.bp))
                    self.stack.print()

            except EndOfProgram:
                return 0
            except Exception as error:
                print("Error at line ({}) - error message '{}'".format(self.pc, error))
                print(self.global_variables)
                self.stack.print()
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_tb(exc_traceback)
                return -1

    def execute(self, byte_code):
        def get_value_from_register(input):
            operator_map = {'+': operator.add, '-': operator.sub}
            symbol_map = {'pc': self.pc, 'bp': self.bp, 'sp': self.stack.sp}

            if input in symbol_map:
                return symbol_map[input]  # pc, bp, sp

            elif '-' in input or '+' in input:
                if '-' in input:
                    reg, offset = input.split('-')
                    op = '-'
                else:
                    reg, offset = input.split('+')
                    op = '+'
                return operator_map[op](symbol_map[reg], int(offset))
            else:
                raise Exception("no supported operation {}".format(input))

        def get_address_or_value(input):
            # if the input starts with [, it means a memory access
            if type(input) is str:
                if input.startswith("["):
                    location = get_value_from_register(input[1:-1])
                    return self.stack[location]
                # because of this bp, sp, pc should be reserved words
                elif input.startswith("bp") or input.startswith("sp") or input.startswith("pc"):
                    return get_value_from_register(input)
                else:
                    return input # global variables

            else:
                return input

        if byte_code.command == "push":
            arg = get_address_or_value(byte_code.arg1)
            self.stack.push(arg)
            return 0

        if byte_code.command == "pop":
            val = self.stack.pop()
            if byte_code.arg1 is not None:
                if byte_code.arg1 == 'bp':
                    self.bp = val
                else:
                    raise Exception("only pop bp supported")
            return 0

        elif byte_code.command == "mov":
            arg1 = byte_code.arg1
            arg2 = byte_code.arg2

            # we support only one mov command
            # mov bp sp-1
            if arg1 == "bp" and arg2 == "sp-1":
                self.bp = self.stack.sp - 1
            else:
                raise Exception("mov {} {} not supported".format(arg1, arg2))
            return 0

        # elif byte_code.command == "location_store":
        #     location = self.stack.pop()
        #     value = self.stack.pop()
        #     self.stack[location] = value
        #     return 0

        elif byte_code.command == "stack_mov":
            arg1 = byte_code.arg1
            if arg1 == "top":
                arg2 = get_address_or_value(byte_code.arg2)
                val = self.stack.pop()
                self.stack[arg2] = val
            return 0

        elif byte_code.command == "pop_n":
            arg1 = byte_code.arg1
            for i in range(arg1):
                self.stack.pop()
            return 0

        elif byte_code.command == "push_n":
            arg1 = byte_code.arg1
            for i in range(arg1):
                self.stack.push(0)
            return 0

        elif byte_code.command == "jmp_from_top":
            arg1 = byte_code.arg1
            return_address = self.stack.pop()
            return return_address

        elif byte_code.command in ["add", "sub", "mul", "div"]:
            v2 = self.stack.pop()
            v1 = self.stack.pop()

            if byte_code.command == "add": self.stack.push(v1 + v2)
            if byte_code.command == "sub": self.stack.push(v1 - v2)
            if byte_code.command == "mul": self.stack.push(v1 * v2)
            if byte_code.command == "div": self.stack.push(v1 / v2)
            return 0

        elif byte_code.command == "value":
            variable = self.stack.pop()
            if variable in self.global_variables.keys():
                self.stack.push(self.global_variables[variable])
            else:
                raise Exception("Variable {} is not defined".format(variable))
            return 0

        elif byte_code.command == "copyarray":
            arrayCopy = self.stack.pop()
            self.global_variables["copyArr"] = arrayCopy
            # self.stack.push(self.global_variables[byte_code.arg1])
            self.global_variables["count"] = 0

            return 0

        elif byte_code.command == "checkarraylength":
            copyArr = self.global_variables["copyArr"]
            count = self.global_variables["count"]
            self.stack.push(len(copyArr) > count)
            return 0

        elif byte_code.command == "get_element_value":
            copyArr = self.global_variables["copyArr"]
            count = self.global_variables["count"]
            elem_value = copyArr[count]
            self.global_variables[byte_code.arg1] = elem_value
            count = count + 1
            self.global_variables["count"] = count

            return 0

        elif byte_code.command == "store":
            variable = self.stack.pop()
            exp = self.stack.pop()
            if variable in self.global_variables.keys():
                self.global_variables[variable] = exp
            else:
                raise Exception("Variable {} is not defined".format(variable))
            return 0

        elif byte_code.command == "create_store":
            variable = self.stack.pop()
            exp = self.stack.pop()
            self.global_variables[variable] = exp
            return 0

        elif byte_code.command == "memory_store":
            loc = self.stack.pop()
            exp = self.stack.pop()
            self.stack[loc] = exp
            return 0

        elif byte_code.command == "print":
            v1 = self.stack.pop()
            print(v1)
            return 0

        elif byte_code.command == "jmp":
            return self.pc + byte_code.arg1 # modify the next pointer

        elif byte_code.command == "if_false_jmp":
            v1 = self.stack.pop()
            if not v1: return (self.pc + byte_code.arg1) # if false jump
            else: return 0

        elif byte_code.command == "lessthan":
            v2 = self.stack.pop()
            v1 = self.stack.pop()
            self.stack.push(v1 < v2)
            return 0

        elif byte_code.command == "morethan":
            v2 = self.stack.pop()
            v1 = self.stack.pop()
            self.stack.push(v1 > v2)
            return 0

        elif byte_code.command == "eq":
            v2 = self.stack.pop()
            v1 = self.stack.pop()
            self.stack.push(v1 == v2)
            return 0

        elif byte_code.command == "not":
            v = self.stack.pop()
            self.stack.push(not v)
            return 0

        elif byte_code.command == "exit":
            raise EndOfProgram("Exit detected")

        else:
            raise Exception("{} byte code does not support".format(byte_code.command))
