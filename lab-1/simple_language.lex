%{
#include "y.tab.h"
%}

%%

[ \t]            ;   // Ignorar espacios y tabs
[a-zA-Z_][a-zA-Z0-9_]*    { yylval.str = strdup(yytext); return VARIABLE; }
[0-9]+                   { yylval.num = atoi(yytext); return NUMBER; }
\n                       { return EOL; }
"+"                      { return '+'; }
"-"                      { return '-'; }
"*"                      { return '*'; }
"/"                      { return '/'; }
"="                      { return '='; }

.                { printf("Caracter no reconocido: %s\n", yytext); return yytext[0]; }

%%

int yywrap() {
    return 1;
}