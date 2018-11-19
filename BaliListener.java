// Generated from /Users/smcho/PycharmProjects/BaliInterpreter/src/ver4/Bali.g4 by ANTLR 4.7
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link BaliParser}.
 */
public interface BaliListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link BaliParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(BaliParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link BaliParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(BaliParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link BaliParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(BaliParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link BaliParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(BaliParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link BaliParser#params}.
	 * @param ctx the parse tree
	 */
	void enterParams(BaliParser.ParamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link BaliParser#params}.
	 * @param ctx the parse tree
	 */
	void exitParams(BaliParser.ParamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link BaliParser#arguments}.
	 * @param ctx the parse tree
	 */
	void enterArguments(BaliParser.ArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link BaliParser#arguments}.
	 * @param ctx the parse tree
	 */
	void exitArguments(BaliParser.ArgumentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link BaliParser#function_body}.
	 * @param ctx the parse tree
	 */
	void enterFunction_body(BaliParser.Function_bodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link BaliParser#function_body}.
	 * @param ctx the parse tree
	 */
	void exitFunction_body(BaliParser.Function_bodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link BaliParser#function_name}.
	 * @param ctx the parse tree
	 */
	void enterFunction_name(BaliParser.Function_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link BaliParser#function_name}.
	 * @param ctx the parse tree
	 */
	void exitFunction_name(BaliParser.Function_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link BaliParser#function_call}.
	 * @param ctx the parse tree
	 */
	void enterFunction_call(BaliParser.Function_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link BaliParser#function_call}.
	 * @param ctx the parse tree
	 */
	void exitFunction_call(BaliParser.Function_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link BaliParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(BaliParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link BaliParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(BaliParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link BaliParser#statements}.
	 * @param ctx the parse tree
	 */
	void enterStatements(BaliParser.StatementsContext ctx);
	/**
	 * Exit a parse tree produced by {@link BaliParser#statements}.
	 * @param ctx the parse tree
	 */
	void exitStatements(BaliParser.StatementsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code assignStatement}
	 * labeled alternative in {@link BaliParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterAssignStatement(BaliParser.AssignStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assignStatement}
	 * labeled alternative in {@link BaliParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitAssignStatement(BaliParser.AssignStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code printStatement}
	 * labeled alternative in {@link BaliParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterPrintStatement(BaliParser.PrintStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code printStatement}
	 * labeled alternative in {@link BaliParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitPrintStatement(BaliParser.PrintStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ifStatement}
	 * labeled alternative in {@link BaliParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(BaliParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ifStatement}
	 * labeled alternative in {@link BaliParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(BaliParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code whileStatement}
	 * labeled alternative in {@link BaliParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(BaliParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code whileStatement}
	 * labeled alternative in {@link BaliParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(BaliParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code expStatement}
	 * labeled alternative in {@link BaliParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterExpStatement(BaliParser.ExpStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code expStatement}
	 * labeled alternative in {@link BaliParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitExpStatement(BaliParser.ExpStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code returnStatement}
	 * labeled alternative in {@link BaliParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatement(BaliParser.ReturnStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code returnStatement}
	 * labeled alternative in {@link BaliParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatement(BaliParser.ReturnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link BaliParser#location}.
	 * @param ctx the parse tree
	 */
	void enterLocation(BaliParser.LocationContext ctx);
	/**
	 * Exit a parse tree produced by {@link BaliParser#location}.
	 * @param ctx the parse tree
	 */
	void exitLocation(BaliParser.LocationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LiteralExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterLiteralExp(BaliParser.LiteralExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LiteralExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitLiteralExp(BaliParser.LiteralExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NotExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterNotExp(BaliParser.NotExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NotExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitNotExp(BaliParser.NotExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AndExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterAndExp(BaliParser.AndExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AndExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitAndExp(BaliParser.AndExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AddExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterAddExp(BaliParser.AddExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AddExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitAddExp(BaliParser.AddExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code DivExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterDivExp(BaliParser.DivExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code DivExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitDivExp(BaliParser.DivExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MulExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterMulExp(BaliParser.MulExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MulExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitMulExp(BaliParser.MulExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code EqExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterEqExp(BaliParser.EqExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code EqExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitEqExp(BaliParser.EqExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FunctionCallExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCallExp(BaliParser.FunctionCallExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FunctionCallExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCallExp(BaliParser.FunctionCallExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LessThanExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterLessThanExp(BaliParser.LessThanExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LessThanExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitLessThanExp(BaliParser.LessThanExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NegExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterNegExp(BaliParser.NegExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NegExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitNegExp(BaliParser.NegExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code OrExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterOrExp(BaliParser.OrExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code OrExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitOrExp(BaliParser.OrExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MoreThanExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterMoreThanExp(BaliParser.MoreThanExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MoreThanExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitMoreThanExp(BaliParser.MoreThanExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ParenthExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterParenthExp(BaliParser.ParenthExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ParenthExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitParenthExp(BaliParser.ParenthExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NotEqExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterNotEqExp(BaliParser.NotEqExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NotEqExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitNotEqExp(BaliParser.NotEqExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LocationExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterLocationExp(BaliParser.LocationExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LocationExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitLocationExp(BaliParser.LocationExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SubExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterSubExp(BaliParser.SubExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SubExp}
	 * labeled alternative in {@link BaliParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitSubExp(BaliParser.SubExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link BaliParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(BaliParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link BaliParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(BaliParser.LiteralContext ctx);
}