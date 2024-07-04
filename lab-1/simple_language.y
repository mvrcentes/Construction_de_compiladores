%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>  
#include <ctype.h>

void yyerror(const char *);
int yylex(void);

// Arreglo para simular una tabla de símbolos
int symbols[256]; // Suficiente espacio para variables con una letra.

int resolve_variable(char* var) {
    int index = var[0] - 'a';  // Asegura que 'a' es 0, 'b' es 1, etc.
    return symbols[index];
}

void set_variable(char* var, int value) {
    int index = var[0] - 'a';  // Asegura que 'a' es 0, 'b' es 1, etc.
    symbols[index] = value;
}
%}

%union {
    int num;
    char* str;
}

%token <str> VARIABLE
%token <num> NUMBER
%token EOL

%left '+' '-'
%left '*' '/'

%type <num> expression

%%

program:
    | program statement
    | program error EOL { yyerrok; } // Continúa después de un error.
    ;

statement:
      VARIABLE '=' expression EOL { set_variable($1, $3); printf("%s = %d\n", $1, $3); }
    ;

expression:
      expression '+' expression { $$ = $1 + $3; }
    | expression '-' expression { $$ = $1 - $3; }
    | expression '*' expression { $$ = $1 * $3; }
    | expression '/' expression { $$ = $1 / $3; }
    | VARIABLE                  { $$ = resolve_variable($1); }
    | NUMBER                    { $$ = $1; }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "%s\n", s);
}

int main(void) {
    memset(symbols, 0, sizeof(symbols)); // Inicializa el arreglo a 0
    yyparse();
    return 0;
}
