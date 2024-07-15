grammar MiniLang;

prog:   stat+ ;

stat:   expr NEWLINE                       # printExpr
    |   ID '=' expr NEWLINE                # assign
    |   IF expr THEN stat+ ('else' stat+)? ENDIF NEWLINE        # IfStatement
    |   WHILE expr DO stat+ ENDWHILE NEWLINE              # WhileStatement
    |   FUNC ID '(' (ID (',' ID)*)? ')' stat+ ENDFUNC NEWLINE # FuncDef
    |   ID '(' (expr (',' expr)*)? ')' NEWLINE                 # FuncCall
    |   NEWLINE                            # blank
    ;

expr:   expr ('*'|'/') expr                # MulDiv
    |   expr ('+'|'-') expr                # AddSub
    |   expr ('=='|'!='|'<'|'>'|'<='|'>=') expr  # Comparison
    |   INT                                # int
    |   STRING                             # string
    |   ID                                 # id
    |   '(' expr ')'                       # parens
    ;

MUL : '*' ; // define token for multiplication
DIV : '/' ; // define token for division
ADD : '+' ; // define token for addition
SUB : '-' ; // define token for subtraction
EQ  : '==' ; // define token for equal comparison
NEQ : '!=' ; // define token for not equal comparison
LT  : '<' ;  // define token for less than comparison
GT  : '>' ;  // define token for greater than comparison
LEQ : '<=' ; // define token for less than or equal comparison
GEQ : '>=' ; // define token for greater than or equal comparison

IF : 'if' ;     // define token if
THEN : 'then' ; // define token then
ELSE : 'else' ; // define token else
ENDIF : 'endif' ; // define token endif
WHILE : 'while' ; // define token while
DO : 'do' ; // define token do
ENDWHILE : 'endwhile' ; // define token endwhile
FUNC : 'func' ;         // define token func
ENDFUNC : 'endfunc' ;   // define token endfunc

ID  : [a-zA-Z]+ ; // match identifiers
STRING : '"' (~['"'|"\r\n"])* '"' ; // string support
INT : [0-9]+ ; // match integers
NEWLINE:'\r'? '\n' ; // return newlines to parser (is end-statement signal)
WS  : [ \t]+ -> skip ; // toss out whitespace

// Regla para comentarios de una sola linea
LINE_COMMENT : '//' ~[\r\n]* -> skip ;