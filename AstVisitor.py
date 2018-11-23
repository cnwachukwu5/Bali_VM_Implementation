from AstNode import *
from BaliParser import BaliParser
from BaliVisitor import BaliVisitor

class AstVisitor(BaliVisitor):
    def __init__(self):
        self.programNode = None

    # program
    #     :  (declaration | statement | function )*
    #     ;
    def visitProgram(self, ctx: BaliParser.ProgramContext):
        nodes = []
        for node in ctx.getChildren():
            nodes.append(self.visit(node))
        self.programNode = ProgramNode(nodes)

    # function
    #     : 'def' function_name '(' params? ')' function_body
    #     ;
    def visitFunction(self, ctx:BaliParser.FunctionContext):
        functionName = ctx.function_name().ID().getText()
        if ctx.params() is not None:
            parameterNodes = self.visit(ctx.params())
        else:
            parameterNodes = None
        bodyNode = self.visit(ctx.function_body())
        return FunctionNode(functionName, parameterNodes, bodyNode)

    # params
    #     : ID (',' ID)*
    #     ;
    def visitParams(self, ctx:BaliParser.ParamsContext):
        result = []
        for id in ctx.ID():
            result.append(id.getText())
        return ParamsNode(result)

    # arguments
    #     : exp ( ',' exp )*
    #     ;
    def visitArguments(self, ctx:BaliParser.ArgumentsContext):
        result = []
        for exp in ctx.exp():
            result.append(self.visit(exp))
        return ArgumentsNode(result)

    # arrayvalues
    #     : (STRING (',' STRING)*)*
    #     | (INTEGER (',' INTEGER)*)*
    #     ;
    def visitArrayvalues(self, ctx: BaliParser.ArrayvaluesContext):
        arrayvalues = []
        # TODO - escape quotes in strings
        if ctx.STRING() is not None:
            for value in ctx.STRING():
                arrayvalues.append(value.getText())

        if ctx.INTEGER() is not None:
            for value in ctx.INTEGER():
                arrayvalues.append(int(value.getText()))

        return ArrayValueNode(arrayvalues)

    # | arrayvalues                                                             # arrayvalueExp
    def visitArrayvalueExp(self, ctx: BaliParser.ArrayvalueExpContext):

        arrayValueNode = None
        if ctx.arrayvalues() is not None:
            arrayValueNode = self.visitArrayvalues(ctx.arrayvalues())

        return ArrayValueExpNode(arrayValueNode.arrayvalue)

    # function_body
    #     : '{' (declaration | statement)* '}'
    #     ;
    def visitFunction_body(self, ctx:BaliParser.Function_bodyContext):
        nodes = []
        declarationsNode = self.visit(ctx.declarations())
        statementsNode = self.visit(ctx.statements())
        return Function_bodyNode(declarationsNode, statementsNode)

    # function_name
    #     : ID
    #     ;
    #

    # declaration
    #     : 'var' location ('=' exp)? ';'
    #     ;
    def visitDeclaration(self, ctx: BaliParser.DeclarationContext):
        variable = ctx.location().getText()
        if ctx.exp() is not None:
            value = self.visit(ctx.exp())
        else:
            value = None
        return DeclarationNode(variable, value)

    # statements
    #     : statement*
    #     ;
    def visitStatements(self, ctx: BaliParser.StatementsContext):
        result = []
        for statement in ctx.statement():
            result.append(self.visit(statement))
        return StatementsNode(result)

    # declarations
    #     : declaration*
    #     ;
    def visitDeclarations(self, ctx: BaliParser.DeclarationsContext):
        result = []
        for declaration in ctx.declaration():
            result.append(self.visit(declaration))
        return DeclarationsNode(result)

    # statement
    #     : location '=' exp ';'                                                   # assignStatement
    def visitAssignStatement(self, ctx: BaliParser.AssignStatementContext):
        location = self.visit(ctx.location())
        exp = self.visit(ctx.exp())
        return AssignStatementNode(location, exp)

    #     | 'print' exp ';'                                                        # printStatement
    def visitPrintStatement(self, ctx: BaliParser.PrintStatementContext):
        exp = ctx.exp()
        node = self.visit(exp)
        return PrintStatementNode(node)

    #     | 'if' '(' exp ')' '{' statements '}' ('else' '{' statements '}')? ';'   # ifStatement
    def visitIfStatement(self, ctx: BaliParser.IfStatementContext):
        exp = self.visit(ctx.exp())
        ifStatements = self.visit(ctx.statements(0))
        if len(ctx.statements()) == 2:
            elseStatements = self.visit(ctx.statements(1))
        else:
            elseStatements = None
        return IfStatementNode(exp, ifStatements, elseStatements)

    #     | 'while' '(' exp ')' '{' statements '}' ';'                             # whileStatement
    def visitWhileStatement(self, ctx: BaliParser.WhileStatementContext):
        exp = self.visit(ctx.exp())
        statements = self.visit(ctx.statements())
        return WhileStatementNode(exp, statements)

    # | 'do' '{' statements '}' 'while' '(' exp ')' ';'                           # doWhileStatement
    def visitDoWhileStatement(self, ctx:BaliParser.DoWhileStatementContext):
        exp = self.visit(ctx.exp())
        statements = self.visit(ctx.statements())
        return DoWhileStatementNode(exp, statements)

    #  | 'foreach' '('location ':' exp ')' '{' statements '}' ';'                 # foreachStatement
    def visitForeachStatement(self, ctx: BaliParser.ForeachStatementContext):
        exp = self.visit(ctx.exp())
        print(type(exp))
        location = self.visit(ctx.location())
        print(type(location))
        statements = self.visit(ctx.statements())
        print(type(statements))

        return ForEachStatementNode(location, exp, statements)

    #     | exp ';'                                                                # expStatement
    def visitExpStatement(self, ctx: BaliParser.ExpStatementContext):
        exp = self.visit(ctx.exp())
        return ExpStatementNode(exp)

    #     | 'return' exp ';'                                                       # returnStatement
    def visitReturnStatement(self, ctx: BaliParser.ReturnStatementContext):
        exp = self.visit(ctx.exp())
        return ReturnStatementNode(exp)

    # location
    #     : ID
    #     ;
    def visitLocation(self, ctx: BaliParser.LocationContext):
        location = ctx.getText()
        return LocationNode(location)

    # function_call
    #     : function_name '(' arguments? ')'
    #     ;
    def visitFunction_call(self, ctx: BaliParser.Function_callContext):
        function_name = ctx.function_name().ID().getText()
        if ctx.arguments() is not None:
            argumentNode = self.visit(ctx.arguments())
        else:
            argumentNode = None
        return Function_callNode(function_name, argumentNode)
    # exp

    # FunctionCallExp
    # function_name '(' arguments? ')'
    def visitFunctionCallExp(self, ctx: BaliParser.FunctionCallExpContext):
        function_call = self.visit(ctx.function_call())
        return FunctionCallExpNode(function_call)

    #     : literal                       # LiteralExp
    def visitLocationExp(self, ctx: BaliParser.LocationExpContext):
        location = ctx.getText()
        return LocationExpNode(location)

    #     | '-' exp                       # NegExp
    def visitNegExp(self, ctx: BaliParser.NegExpContext):
        exp = self.visit(ctx.exp())
        zero = LiteralNode('int', 0)
        return BinOpNode('-', zero, exp)

    #     | '!' exp                       # NotExp
    def visitNotExp(self, ctx: BaliParser.NotExpContext):
        exp = self.visit(ctx.exp())
        return UnaryOpNode('not', exp)

    def binOpNode(self, ctx, op):
        node1 = self.visit(ctx.exp(0))
        node2 = self.visit(ctx.exp(1))
        return BinOpNode(op, node1, node2)

    #     | exp '+' exp                   # AddExp
    def visitAddExp(self, ctx: BaliParser.AddExpContext):
        return self.binOpNode(ctx, 'add')

    #     | exp '-' exp                   # SubExp
    def visitSubExp(self, ctx: BaliParser.AddExpContext):
        return self.binOpNode(ctx, 'sub')

    #     | exp '*' exp                   # MulExp
    def visitMulExp(self, ctx: BaliParser.MulExpContext):
        return self.binOpNode(ctx, 'mul')

    #     | exp '/' exp                   # DivExp
    def visitDivExp(self, ctx: BaliParser.DivExpContext):
        return self.binOpNode(ctx, 'div')

    #     | exp '&' exp                   # AndExp
    def visitAndExp(self, ctx: BaliParser.LessThanExpContext):
        return self.binOpNode(ctx, 'and')

    #     | exp '|' exp                   # OrExp
    def visitAndExp(self, ctx: BaliParser.LessThanExpContext):
        return self.binOpNode(ctx, 'or')

    #     | exp '<' exp                   # LessThanExp
    def visitLessThanExp(self, ctx: BaliParser.LessThanExpContext):
        return self.binOpNode(ctx, 'lessthan')

    #     | exp '>' exp                   # MoreThanExp
    def visitMoreThanExp(self, ctx: BaliParser.MoreThanExpContext):
        return self.binOpNode(ctx, 'morethan')

    #     | exp '==' exp                  # EqExp
    def visitEqExp(self, ctx: BaliParser.EqExpContext):
        return self.binOpNode(ctx, 'eq')

    #     | exp '!=' exp                  # NotEqExp
    def visitNotEqExp(self, ctx: BaliParser.NotEqExpContext):
        return self.binOpNode(ctx, 'neq')

    #     | '(' exp ')'                   # ParenthExp
    def visitParenthExp(self, ctx: BaliParser.ParenthExpContext):
        return self.visit(ctx.exp())

    # literal
    #     : INTEGER | 'True' | 'False' | STRING
    def visitLiteralExp(self, ctx: BaliParser.LiteralContext):
        txt = ctx.getText()
        if txt in ['True', 'False']:
            literalType = 'boolean'
            value = txt
        elif txt.isnumeric():
            literalType = 'int'
            value = int(txt)
        else:
            literalType = 'str'
            value = txt
        return LiteralNode(literalType, value)