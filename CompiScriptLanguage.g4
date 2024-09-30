grammar CompiScriptLanguage;

program: declaration* EOF ;

declaration: 
    classDecl       # classDeclaration
    |   funDecl     # functionDeclaration
    |   varDecl     # variableDeclaration
    |   statement   # statementDeclaration
    ;

classDecl       : 'class' IDENTIFIER ('extends' IDENTIFIER)? '{' function* '}' ;
funDecl         : 'fun' function ;
varDecl         : 'var' (IDENTIFIER | arrayAccess) ('=' expression)? ';' ;

statement: 
    exprStmt        # expressionStatement
    | forStmt       # forStatement
    | ifStmt        # ifStatement
    | printStmt     # printStatement
    | returnStmt    # returnStatement
    | whileStmt     # whileStatement
    | block         # blockStatement
    ;

exprStmt        : expression ';' ;
forStmt         : 'for' '(' (varDecl | exprStmt | ';') expression? ';' expression? ')' statement ;
ifStmt          : 'if' '(' expression ')' statement ('else' statement)? ;
printStmt       : 'print' expression ';' ;
returnStmt      : 'return' expression? ';' ;
whileStmt       : 'while' '(' expression ')' statement ;
block           : '{' declaration* '}' ;

expression      :  assignment   # assignmentExp
                | funAnon       # funAnonExp
                ;

funAnon         : 'fun' '(' parameters? ')' block;

assignment      : (call '.')? IDENTIFIER '=' assignment   # nestedAssignment
                | logic_or                                # logicOrAssignment
                | arrayAccess '=' expression              # arrayAssignment
                ;

arrayAccess     : IDENTIFIER '[' NUMBER ']' ;

logic_or        : logic_and ('or' logic_and)* ;
logic_and       : equality ('and' equality)* ;
equality        : comparison (( '!=' | '==' ) comparison)* ;
comparison      : term (( '>' | '>=' | '<' | '<=' ) term)* ;
term            : factor (( '-' | '+' ) factor)* ;
factor          : unary (( '/' | '*' | '%' ) unary)* ;
unary           : ( '!' | '-' ) unary   # nestedUnary
                | call                  # callUnary
                ;
call            :   primary ( '(' arguments? ')' | '.' IDENTIFIER )* # primaryCall
                | funAnon                                            # funAnonCall
                ;

primary: 'true'                    # true
        | 'false'                  # false
        | 'nil'                    # nil
        | 'this'                   # this
        | NUMBER                   # number
        | STRING                   # string
        | IDENTIFIER               # id 
        | '(' expression ')'       # nestedExpression
        | 'super' '.' IDENTIFIER   # super
        | newExpression            # newInstance
        | array                    # newArray
        | arrayAccess              # primaryArrayAccess
        ;

newExpression   : 'new' IDENTIFIER '(' arguments? ')' ;
function        : IDENTIFIER '(' parameters? ')' block ;
parameters      : IDENTIFIER ( ',' IDENTIFIER )* ;
arguments       : expression ( ',' expression )* ;

array           : '[' (expression (',' expression)*)? ']';

NUMBER          : DIGIT+ ( '.' DIGIT+ )? ;
STRING          : '"' (~["\\])* '"' ;
IDENTIFIER      : ALPHA ( ALPHA | DIGIT )* ;
fragment ALPHA  : [a-zA-Z_] ;
fragment DIGIT  : [0-9] ;
WS              : [ \t\r\n]+ -> skip ;

// One line comments
LINE_COMMENT    : '//' ~[\r\n]* -> skip ;