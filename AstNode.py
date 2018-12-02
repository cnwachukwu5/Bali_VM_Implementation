class Node(object):
    def accept(self, visitor):
        raise Exception("accept not implemented")


# program
#     :  (declaration | statement | function )*
#     ;
class ProgramNode(Node):
    def __init__(self, nodes):
        self.nodes = nodes

    def accept(self, visitor):
        return visitor.visitProgram(self)


# function
#     : 'def' function_name '(' params? ')' function_body
#     ;
class FunctionNode(Node):
    def __init__(self, functionName, paramsNode, function_bodyNode):
        self.functionName = functionName
        self.paramsNode = paramsNode
        self.function_bodyNode = function_bodyNode

    def accept(self, visitor):
        return visitor.visitFunction(self)

    def get_parameter_names(self):
        if self.paramsNode is not None:
            return self.paramsNode.parameters
        return []

    def get_local_variable_names(self):
        return [node.location for node in self.function_bodyNode.declarationsNode.declarationNodes]


# params
#     : ID (',' ID)*
#     ;
class ParamsNode(Node):
    def __init__(self, parameters):
        self.parameters = parameters  # parameters is a list of ID()

    def accept(self, visitor):
        return visitor.visitParams(self)


# function_call
#     : function_name '(' arguments? ')'
#     ;
class Function_callNode(Node):
    def __init__(self, function_name, argumentsNode):
        self.function_name = function_name
        self.argumentsNode = argumentsNode

    def accept(self, visitor):
        return visitor.visitFunction_call(self)


# arguments
#     : exp ( ',' exp )*
#     ;
class ArgumentsNode(Node):
    def __init__(self, argumentNodes):
        self.argumentNodes = argumentNodes

    def accept(self, visitor):
        return visitor.visitArguments(self)


# function_body
#     : '{' declarations statements '}'
#     ;
class Function_bodyNode(Node):
    def __init__(self, declarationsNode, statementsNode):
        self.declarationsNode = declarationsNode
        self.statementsNode = statementsNode

    def accept(self, visitor):
        return visitor.visitFunction_body(self)


class StatementNode(Node):
    pass


# declaration
#     : 'var' location ('=' exp)? ';'
#     ;
class DeclarationNode(Node):
    def __init__(self, location, exp):
        self.location = location
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitDeclaration(self)


# statements
#     : statement*
#     ;
class StatementsNode(Node):
    def __init__(self, statements):
        self.statements = statements

    def accept(self, visitor):
        return visitor.visitStatements(self)


# declarations
#     : declaration*
#     ;
class DeclarationsNode(Node):
    def __init__(self, declarationNodes):
        self.declarationNodes = declarationNodes

    def accept(self, visitor):
        return visitor.visitDeclarations(self)

    def accept(self, visitor):
        return visitor.visitStatements(self)


#     : location '=' exp ';'                                                   # assignStatement
class AssignStatementNode(StatementNode):
    def __init__(self, location, exp):
        self.location = location
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitAssignStatement(self)


#     | 'print' exp ';'                                                        # printStatement
class PrintStatementNode(StatementNode):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitPrintStatement(self)


#  | 'foreach' '('location ':' exp ')' '{' statements '}' ';'               # foreachStatement
class ForEachStatementNode(StatementNode):
    def __init__(self, location, exp, statements):
        self.location = location
        self.exp = exp
        self.statements = statements

    def accept(self, visitor):
        return visitor.visitForeachStatement(self)


#     | 'if' '(' exp ')' '{' statements '}' ('else' '{' statements '}')? ';'   # ifStatement
class IfStatementNode(StatementNode):
    def __init__(self, exp, ifStatements, elseStatements):
        self.exp = exp
        self.ifStatements = ifStatements
        self.elseStatements = elseStatements

    def accept(self, visitor):
        return visitor.visitIfStatement(self)


# case exp : statements break;
class CaseStatementNode(StatementNode):
    def __init__(self, exp, caseStatements):
        self.exp = exp
        self.caseStatements = caseStatements


    def accept(self, visitor):
        return visitor.visitCaseStatement(self)

 # switch ( exp ) { casestatement1, casestatement2.... } ;
class SwitchStatementNode(StatementNode):
    def __init__(self, exp, caseStatements, defaultStatements):
        self.exp = exp
        self.defaultStatements = defaultStatements
        self.caseStatements = caseStatements

    def accept(self, visitor):
        return visitor.visitSwitchStatement(self)


#      | 'while' '(' exp ')' '{' statements '}' ';'                             # whileStatement
class WhileStatementNode(StatementNode):
    def __init__(self, exp, statements):
        self.exp = exp
        self.statements = statements

    def accept(self, visitor):
        return visitor.visitWhileStatement(self)


# | 'do' '{' statements '}' 'while' '(' exp ')' ';'                        # doWhileStatement
class DoWhileStatementNode(StatementNode):
    def __init__(self, exp, statements):
        self.exp = exp
        self.statements = statements

    def accept(self, visitor):
        return visitor.visitDoWhileStatement(self)


#    | exp ';'                                                                # expStatement
class ExpStatementNode(StatementNode):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitExpStatement(self)


#     | 'return' exp ';'                                                       # returnStatement
class ReturnStatementNode(StatementNode):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitReturnStatement(self)


# location
#     : ID
#     ;
class LocationNode(Node):
    def __init__(self, location):
        self.location = location

    def accept(self, visitor):
        return visitor.visitLocation(self)


# arrayvalue
#     : STRING (',' STRING)*
#     | INTEGER (',' INTEGER)*
#     ;
class ArrayValueNode(Node):
    def __init__(self, arrayvalue):
        self.arrayvalue = arrayvalue

    def accept(self, visitor):
        return visitor.visitArrayvalues(self)


# | arrayvalues                                                                            # arrayvalueExp
class ArrayValueExpNode(Node):
    def __init__(self, arrayvalues):
        self.arrayvalues = arrayvalues

    def accept(self, visitor):
        return visitor.visitArrayvalueExp(self)


# : function_call                 # FunctionCallExp
class FunctionCallExpNode(Node):
    def __init__(self, function_call):
        self.function_call = function_call

    def accept(self, visitor):
        return visitor.visitFunctionCallExp(self)


#    | location                      # LocationExp
class LocationExpNode(Node):
    def __init__(self, location):
        self.location = location

    def accept(self, visitor):
        return visitor.visitLocationExp(self)


#    | literal                       # LiteralExp
class LiteralExpNode(Node):
    def __init__(self, literal):
        self.location = literal

    def accept(self, visitor):
        return visitor.visitLiteralExp(self)


class UnaryOpNode(Node):
    def __init__(self, op, exp):
        self.op = op
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitUnaryOp(self)


class BinOpNode(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visitBinOp(self)


# literal
#     : INTEGER | 'True' | 'False'
#     ;
class LiteralNode(Node):
    def __init__(self, literalType: str, value):
        self.literalType = literalType
        self.value = value

    def accept(self, visitor):
        return visitor.visitLiteral(self)
