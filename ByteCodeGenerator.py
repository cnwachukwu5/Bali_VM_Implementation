from AstNode import FunctionNode
from Info import FunctionsInfo, FunctionInfo

label = 0


def get_label():
    global label
    label += 1
    return label


class ByteCode(object):
    def __init__(self, command, arg1=None, arg2=None):
        self.command = command
        self.arg1 = arg1
        self.arg2 = arg2


class ByteCodeGenerator(object):
    def __init__(self):
        self.global_variables = []  # global variables
        self.current_function_name = ""
        self.functions_info = FunctionsInfo()  # stores the name of the function -> number of parameters

    #########################################
    # UTILITIES
    #########################################

    def get_number_of_parameters(self, function_name=None):
        if function_name is None: function_name = self.current_function_name
        return self.functions_info.get_number_of_parameters(function_name)

    def get_number_of_local_variables(self, function_name=None):
        if function_name is None: function_name = self.current_function_name
        return self.functions_info.get_number_of_local_variables(function_name)

    def find_variable(self, location_name):

        # For example with x = y;
        # we need to know if y is a local/parameter/global variable name
        # when y is a global -> x
        # when y is a local or parametr -> bp+? or bp-? (? will be replaced by a number)

        # check local variables or parameters
        if self.current_function_name:
            # check if this is a variable or parameter name
            try:
                search_name = self.functions_info.get_local_location(self.current_function_name, location_name)
                return search_name
            except Exception:
                # in a function, the name should be already declared in a global scope
                if location_name in self.global_variables:
                    return location_name

        return location_name

    def find_value(self, location_name):
        if self.current_function_name:
            # check if this is a variable name
            try:
                search_name = self.functions_info.get_local_value(self.current_function_name, location_name)
                return search_name
            except Exception:
                if location_name in self.global_variables:
                    return location_name

        if location_name in self.global_variables:
            return location_name
        raise Exception("{} is not in global/local/parameter of {} global_variables: {}".format(location_name,
                                                                                                self.current_function_name,
                                                                                                self.global_variables))

    def set_location_name(self, location_name):
        if self.current_function_name:
            name = self.functions_info.get_local_variable_location(self.current_function_name, location_name)
        else:
            name = location_name
        # self.variables.append(name)
        return name

    # def find_location(self, name):
    #     pass
    #
    # def find_value(self, name):
    #     pass

    #########################################
    # VISITORS
    #########################################

    def visit(self, node):
        return node.accept(self)

    def visitProgram(self, programNode):
        code = []
        function_code = []
        nodes = programNode.nodes
        for node in nodes:
            if isinstance(node, FunctionNode):
                function_code += self.visit(node)
            else:
                code += self.visit(node)
        code += [ByteCode("exit")]

        code += function_code
        return code

    # function
    #     : 'def' function_name '(' params? ')' function_body
    #     ;
    def visitFunction(self, functionNode):
        self.current_function_name = functionNode.functionName
        function_name_label = ":" + functionNode.functionName

        local_variable_names = functionNode.get_local_variable_names()
        parameter_names = functionNode.get_parameter_names()
        number_of_local_variables = len(local_variable_names)

        self.functions_info[functionNode.functionName] = FunctionInfo(functionNode.functionName,
                                                                      parameter_names,
                                                                      local_variable_names)

        code = [ByteCode("----"), ByteCode(function_name_label), ByteCode("push", "bp"), ByteCode("mov", "bp", "sp-1")]

        if number_of_local_variables > 0:
            code += [ByteCode("push_n", number_of_local_variables)]

        code += self.visit(functionNode.function_bodyNode)

        # reset the function node
        self.current_function_name = ""
        return code

    def visitFunction_call(self, function_callNode):
        code = []
        number_of_arguments = self.get_number_of_parameters(function_callNode.function_name)
        argument_code = []
        if function_callNode.argumentsNode is not None:
            argument_code += self.visit(function_callNode.argumentsNode)

        function_name_label = ":" + function_callNode.function_name
        code += [ByteCode("push", 0)]  # default return value is 0
        code += argument_code
        code += [ByteCode("push", "pc+2")]  # return address
        code += [ByteCode("jmp", function_name_label)]  # , callstack_data)]
        if number_of_arguments > 0:
            code += [ByteCode("pop_n", number_of_arguments)]

        return code

    def visitArguments(self, argumentsNode):
        code = []
        for node in argumentsNode.argumentNodes:
            code += self.visit(node)
        return code

    def visitArrayvalueExp(self, ArrayValueExpNode):
        code = []
        arrayvalues = ArrayValueExpNode.arrayvalues
        code += [ByteCode("push", arrayvalues)]
        return code

    def visitFunction_body(self, function_bodyNode):
        code = []
        for node in function_bodyNode.declarationsNode.declarationNodes:
            code += self.visit(node)
        for node in function_bodyNode.statementsNode.statements:
            code += self.visit(node)
        return code

    def visitParams(self, paramsNode):
        code = []
        return code

    def visitExpStatement(self, expStatementNode):
        code = self.visit(expStatementNode.exp)
        return code

    def visitReturnStatement(self, returnStatementNode):
        code = self.visit(returnStatementNode.exp)
        number_of_local_variables = self.get_number_of_local_variables()
        number_of_arguments = self.get_number_of_parameters()
        location_of_return_value = "bp-" + str(2 + number_of_arguments)
        code += [ByteCode("stack_mov", "top", location_of_return_value)]
        if number_of_local_variables:
            code += [ByteCode("pop_n", number_of_local_variables)]
        code += [ByteCode("pop", "bp"), ByteCode("jmp_from_top")]
        return code

    def visitFunctionCallExp(self, functionCallExpNode):
        code = self.visit(functionCallExpNode.function_call)
        return code

    def visitDeclaration(self, declarationNode):
        code = self.visit(declarationNode.exp)
        code += [ByteCode("push", self.find_variable(declarationNode.location))]
        if self.current_function_name:
            code += [ByteCode("memory_store")]
        else:
            self.global_variables.append(declarationNode.location)
            code += [ByteCode("create_store")]
        return code

    def visitStatements(self, statementsNode):
        code = []
        statements = statementsNode.statements
        for statementNode in statements:
            code += self.visit(statementNode)
        return code

    def visitIfStatement(self, statementNode):
        decision = self.visit(statementNode.exp)
        if_case = self.visit(statementNode.ifStatements)
        if statementNode.elseStatements is not None:
            else_case = self.visit(statementNode.elseStatements)
        else:
            else_case = []

        false_block_label = ":false_block{}".format(get_label())
        end_label = ":end{}".format(get_label())

        code = decision + [ByteCode("if_false_jmp", false_block_label)] + \
               if_case + [ByteCode("jmp", end_label), ByteCode(false_block_label)] + \
               else_case + [ByteCode(end_label)]
        return code

    def visitSwitchStatement(self, statementNode):
        decision = self.visit(statementNode.exp)
        caseStatements = self.visit(statementNode.caseStatements)
        defaultStatements = self.visit(statementNode.defaultStatements)
        code = decision + caseStatements + defaultStatements
        return code

    def visitCaseStatement(self, statementNode):
        decision = self.visit(statementNode.exp)
        case = self.visit(statementNode.caseStatements)
        code = decision + case
        return code

    def visitWhileStatement(self, statementNode):
        decision = self.visit(statementNode.exp)
        statements = self.visit(statementNode.statements)

        start_label = ":start{}".format(get_label())
        end_label = ":end{}".format(get_label())

        code = [ByteCode(start_label)] + decision + \
               [ByteCode("if_false_jmp", end_label)] + \
               statements + \
               [ByteCode("jmp", start_label), ByteCode(end_label)]
        return code

    def visitDoWhileStatement(self, statementNode):
        decision = self.visit(statementNode.exp)
        statements = self.visit(statementNode.statements)

        start_label = ":start{}".format(get_label())
        end_label = ":end{}".format(get_label())

        code = [ByteCode(start_label)] + statements + \
               decision + \
               [ByteCode("if_false_jmp", end_label)] + \
               [ByteCode("jmp", start_label), ByteCode(end_label)]

        return code

    def visitForeachStatement(self, statementNode):
        code = []

        array_ref = self.find_value(statementNode.exp.location)
        location = statementNode.location.location
        statements = self.visit(statementNode.statements)

        start_label = ":start{}".format(get_label())
        end_label = ":end{}".format(get_label())

        code += [ByteCode("push", array_ref)]
        code += [ByteCode("value")]
        code += [ByteCode("copyarray", array_ref)]
        code += [ByteCode(start_label)]
        code += [ByteCode("checkarraylength")]
        code += [ByteCode("if_false_jmp", end_label)]
        code += [ByteCode("get_element_value", location)]
        code += statements
        code += [ByteCode("jmp", start_label), ByteCode(end_label)]

        return code

    def visitPrintStatement(self, statementNode):
        code = self.visit(statementNode.exp) + [ByteCode("print")]
        return code

    def visitAssignStatement(self, statementNode):
        code1 = self.visit(statementNode.exp)
        code2 = self.visit(statementNode.location)
        if code2[0].arg1.startswith("bp"):  # local variable or parameter
            bytecode = [ByteCode("memory_store")]
        else:
            bytecode = [ByteCode("store")]
        code = code1 + code2 + bytecode
        return code

    def visitLocation(self, locationNode):
        location_name = self.find_variable(locationNode.location)
        code = [ByteCode("push", location_name)]
        return code

    def visitLocationExp(self, locationExpNode):
        location_name = self.find_value(locationExpNode.location)
        code = [ByteCode("push", location_name)]
        if not (location_name.startswith("[")):
            code += [ByteCode("value")]
        return code

    def visitBinOp(self, expression):
        code1 = self.visit(expression.left)
        code2 = self.visit(expression.right)

        code = code1 + code2 + [ByteCode(expression.op)]
        return code

    def visitUnaryOp(self, unaryOp):
        code = self.visit(unaryOp.exp) + [ByteCode(unaryOp.op)]
        return code

    def visitLiteralExp(self, expression):
        code = [ByteCode("push", expression.literal.value)]
        return code

    def visitLiteral(self, expression):
        code = [ByteCode("push", expression.value)]
        return code
