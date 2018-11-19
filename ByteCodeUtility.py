import copy
class ByteCodeUtility(object):
    def __init__(self, bytecode):
        self.bytecode = bytecode
        self.resolved_bytecode = self.resolve_label()

    def print(self, original = True):
        if original:
            bytecode_source = self.bytecode
            for bytecode in bytecode_source:
                command = "{} ".format(bytecode.command)
                if bytecode.arg1 is not None: command += ": {}".format(bytecode.arg1)
                if bytecode.arg2 is not None: command += " | {}".format(bytecode.arg2)
                print(command)
        else:
            bytecode_source = self.resolved_bytecode
            for i, bytecode in enumerate(bytecode_source):
                command = "{0:2d}: {1} ".format(i, bytecode.command)
                if bytecode.arg1 is not None: command += ": {}".format(bytecode.arg1)
                if bytecode.arg2 is not None: command += " | {}".format(bytecode.arg2)
                print(command)

    def resolve_label(self):
        # 1. map the label names and index
        self.resolved_bytecode = []
        map_label_index = {}
        count = 0
        for bytecode in self.bytecode:
            if bytecode.command.startswith(":"):
                map_label_index[bytecode.command] = count
            elif bytecode.command.startswith("-"):
                pass
            else:
                count += 1
                self.resolved_bytecode.append(copy.copy(bytecode)) # deep copy is needed as the label resolution will modify the original code

        # 2. replace the label with the difference between current poisition and the label position
        count = 0
        for bytecode in self.resolved_bytecode:
            if str(bytecode.arg1).startswith(":"):
                label_position = map_label_index[bytecode.arg1]
                bytecode.arg1 = label_position - count
                #print(bytecode.arg1)
            count += 1

        return self.resolved_bytecode