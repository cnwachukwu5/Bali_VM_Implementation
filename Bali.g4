grammar Bali;

program    
    :  (declaration | statement | function )*
    ;

function
    : 'def' function_name '(' params? ')' function_body
    ;

params
    : ID (',' ID)*
    ;

arguments
    : exp ( ',' exp )*
    ;

function_body
    : '{' declarations statements '}'
    ;

function_name
    : ID
    ;

function_call
    : function_name '(' arguments? ')'
    ;

declaration
    : 'var' location '=' exp ';'
    ;

declarations
    : declaration*
    ;

statements
    : statement*
    ;

statement
    : location '=' exp ';'                                                   # assignStatement
    | 'print' exp ';'                                                        # printStatement
    | 'if' '(' exp ')' '{' statements '}' ('else' '{' statements '}')? ';'   # ifStatement
    | 'while' '(' exp ')' '{' statements '}' ';'                             # whileStatement
    | exp ';'                                                                # expStatement
    | 'return' exp ';'                                                       # returnStatement
    | 'do' '{' statements '}' 'while' '(' exp ')' ';'                        # doWhileStatement
    | 'foreach' '('location ':' exp ')' '{' statements '}' ';'               # foreachStatement
    ;

location
    : ID
    ;

arrayvalues
    : (STRING (',' STRING)*)*
    | (INTEGER (',' INTEGER)*)*
    ;

exp
    : function_call                 # FunctionCallExp
    | location                      # LocationExp
    | '{'arrayvalues'}'             # arrayvalueExp
    | literal                       # LiteralExp
    | '-' exp                       # NegExp
    | '!' exp                       # NotExp
    | exp '+' exp                   # AddExp
    | exp '-' exp                   # SubExp
    | exp '*' exp                   # MulExp
    | exp '/' exp                   # DivExp
    | exp '&' exp                   # AndExp
    | exp '|' exp                   # OrExp
    | exp '<' exp                   # LessThanExp
    | exp '>' exp                   # MoreThanExp
    | exp '==' exp                  # EqExp
    | exp '!=' exp                  # NotEqExp
    | '(' exp ')'                   # ParenthExp
    ;

literal
    : INTEGER | 'True' | 'False' | STRING
    ;

INTEGER
    : '-'? DIGIT+
    ;

STRING
    : '"'.*?'"'|'\''.*?'\''
    ;

ID
    : LETTER (LETTER|DIGIT|'_')*
    ;

WS  :   [ \t\n\r]+ -> skip ;

// PREPROC : '#' .*? '\n' '\r'? -> skip ;
COMMENT : '#' ~[\n\r]* -> skip;
MULTILINE_COMMENT : '/*' .*? '*/' -> skip ;

// fragments

fragment DIGIT : [0-9] ;
fragment LETTER : [a-zA-Z] ;