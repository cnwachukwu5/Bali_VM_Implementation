# Generated from /Users/smcho/PycharmProjects/BaliInterpreter5/src/Bali.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BaliParser import BaliParser
else:
    from BaliParser import BaliParser

# This class defines a complete generic visitor for a parse tree produced by BaliParser.

class BaliVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BaliParser#program.
    def visitProgram(self, ctx:BaliParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#function.
    def visitFunction(self, ctx:BaliParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#params.
    def visitParams(self, ctx:BaliParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#arguments.
    def visitArguments(self, ctx:BaliParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#function_body.
    def visitFunction_body(self, ctx:BaliParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#function_name.
    def visitFunction_name(self, ctx:BaliParser.Function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#function_call.
    def visitFunction_call(self, ctx:BaliParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#declaration.
    def visitDeclaration(self, ctx:BaliParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#declarations.
    def visitDeclarations(self, ctx:BaliParser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#statements.
    def visitStatements(self, ctx:BaliParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#assignStatement.
    def visitAssignStatement(self, ctx:BaliParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#printStatement.
    def visitPrintStatement(self, ctx:BaliParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#ifStatement.
    def visitIfStatement(self, ctx:BaliParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#whileStatement.
    def visitWhileStatement(self, ctx:BaliParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#expStatement.
    def visitExpStatement(self, ctx:BaliParser.ExpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#returnStatement.
    def visitReturnStatement(self, ctx:BaliParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#location.
    def visitLocation(self, ctx:BaliParser.LocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#LiteralExp.
    def visitLiteralExp(self, ctx:BaliParser.LiteralExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#NotExp.
    def visitNotExp(self, ctx:BaliParser.NotExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#AndExp.
    def visitAndExp(self, ctx:BaliParser.AndExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#AddExp.
    def visitAddExp(self, ctx:BaliParser.AddExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#DivExp.
    def visitDivExp(self, ctx:BaliParser.DivExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#MulExp.
    def visitMulExp(self, ctx:BaliParser.MulExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#EqExp.
    def visitEqExp(self, ctx:BaliParser.EqExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#FunctionCallExp.
    def visitFunctionCallExp(self, ctx:BaliParser.FunctionCallExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#LessThanExp.
    def visitLessThanExp(self, ctx:BaliParser.LessThanExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#NegExp.
    def visitNegExp(self, ctx:BaliParser.NegExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#OrExp.
    def visitOrExp(self, ctx:BaliParser.OrExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#MoreThanExp.
    def visitMoreThanExp(self, ctx:BaliParser.MoreThanExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#ParenthExp.
    def visitParenthExp(self, ctx:BaliParser.ParenthExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#NotEqExp.
    def visitNotEqExp(self, ctx:BaliParser.NotEqExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#LocationExp.
    def visitLocationExp(self, ctx:BaliParser.LocationExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#SubExp.
    def visitSubExp(self, ctx:BaliParser.SubExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BaliParser#literal.
    def visitLiteral(self, ctx:BaliParser.LiteralContext):
        return self.visitChildren(ctx)



del BaliParser