grammar MiniLang;

prog:   stat+ ;

stat:   IF expr THEN stat+ (ELSE stat+)? ENDIF NEWLINE # If
    |   expr NEWLINE                 # printExpr
    |   ID '=' expr NEWLINE          # assign
    |   NEWLINE                      # blank
    ;

expr: '(' expr ')'                   #parens
    |   expr ('*'|'/') expr          # MulDiv
    |   expr ('+'|'-') expr          # AddSub
    |   INT                          # int
    |   ID                           # id
    |   expr ('=='|'!='|'<'|'>'|'<='|'>=') expr  # Comp
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
ID  : [a-zA-Z]+ ; // match identifiers
INT : [0-9]+ ; // match integers
IF  : 'if' ; // define token if
THEN  : 'then' ; // define token then
ELSE  : 'else' ; // define token else
ENDIF  : 'endif' ; // define token endif
NEWLINE:'\r'? '\n' ; // return newlines to parser (is end-statement signal)

WS  : [ \t]+ -> skip ; // toss out whitespace
LINE_COMMENT : '//' ~[\r\n]* -> skip ; // toss out line comment