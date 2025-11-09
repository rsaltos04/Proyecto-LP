from zoneinfo import ZoneInfo
import ply.lex as lex
from datetime import datetime
import os

# Inicio del avance 1 por parte de Jefferson Saltos
reserved = {
   "fun": "FUNCTION",
   'if' : 'IF',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'for' : 'FOR',
   'val' : 'VAL',
   'var' : 'VAR',
   'in' : 'IN',
   'return' : 'RETURN',
}

# List of token names.   This is always required
tokens = (
   'COLON',
   'SEMICOLON',
   'INTEGER',
   'FLOAT',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'LBRACE',
   'RBRACE',
   'LBRACKET',
   'RBRACKET',
   'IDENTIFIER',
   'LESS_THAN',
   'BOOLEAN',
   "GREATER_THAN",
   "MOD",
   "STRING",
   "MUTABLE_LIST",
   "MUTABLE_MAP",
   "AND",
   "OR",
   "NOT",
   "GREATER_OR_EQUAL",
   "LESS_OR_EQUAL",
   "ASSIGMENT",
   "EQUALS_TO",
   "NOT_EQUALS",
   "COMMENT_ONE_LINE",
   "COMMENT_MULTIPLE_LINES",
   "RANGE",
   "COMMA",
   "PRINT",
   "PRINTLN",
   "READLN",
) + tuple(reserved.values())

# Regular expression rules for simple tokens
t_COMMA = r","
t_COLON= r':'
t_RANGE = r"\.\."
t_SEMICOLON= r';'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'\/'
t_MOD=r"%"
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE= r'{'
t_RBRACE= r'}'
t_LBRACKET= r'\['
t_RBRACKET= r'\]'
t_LESS_THAN= r'<'
t_GREATER_THAN=r">"
t_AND=r'&&'
t_OR=r'\|\|'
t_NOT=r'!'
t_ASSIGMENT=r'='
t_COMMENT_ONE_LINE=r'\/\/.*'
t_COMMENT_MULTIPLE_LINES=r'\/\*[^\*\/]*\*\/'
    
#Fin de avance 1 por parte de Jefferson Saltos

#Inicio de avance 1 por parte de Steve Robinson

def t_MUTABLE_LIST(t):
    r'MutableList'
    return t

def t_MUTABLE_MAP(t):
    r'MutableMap'
    return t


def t_GREATER_OR_EQUAL(t):
    r'>='
    return t

def t_LESS_OR_EQUAL(t):
    r'<='
    return t

def t_EQUALS_TO(t):
    r'=='
    return t

def t_NOT_EQUALS(t):
    r'!='
    return t

def t_BOOLEAN(t):
    r'(true|false)'
    return t

def t_STRING(t):
    #r'"[.\s]*"'
    r'"[^"]*"'
    t.value=t.value[1:-1]
    return t

def t_IDENTIFIER(t):
    r'[A-Za-z$_][\w$]*'
    t.type= reserved.get(t.value,"IDENTIFIER")
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value=float(t.value)
    return t

# A regular expression rule with some action code
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_PRINT(t):
    r'print'
    return t

def t_PRINTLN(t):
    r'println'
    return t

def t_READLN(t):
    r'readln'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print(f"Caracter lexico no existente '{t.value[0]}' en el lenguaje Kotlin en línea {t.lineno}, posición {t.lexpos}")
    t.lexer.skip(1)
    return f"Caracter lexico no existente '{t.value[0]}' en el lenguaje Kotlin en línea {t.lineno}, posición {t.lexpos}"

# Build the lexer
lexer = lex.lex()

'''
with open('algoritmos/ByeWorld.kt', 'r') as file:
    all_lines = file.readlines()
    data = "".join(all_lines)

# Give the lexer some input
lexer.input(data)

# Tokenize

tokens_reconocidos = []
errores = []

while True:
    tok = lexer.token()
    if not tok:
        break
    if isinstance(tok, str):  # error
        errores.append(tok)
    else:
        tokens_reconocidos.append(f"{tok.type}: {tok.value}")

# === Generar nombre de archivo ===
usuario_git = "stikrobinson"
ecuador_tz = ZoneInfo("America/Guayaquil")
ahora = datetime.now(ecuador_tz)
nombre_archivo = f"lexico-{usuario_git}-{ahora.strftime('%d-%m-%Y-%Hh%M')}.txt"
ruta = f"logs/{nombre_archivo}"

# === Escribir log ===
with open(ruta, "w", encoding="utf-8") as f:
    f.write("TOKENS RECONOCIDOS:\n")
    for token in tokens_reconocidos:
        f.write(token + "\n")
    if len(errores) != 0:
        f.write("\nERRORES:\n")
        for error in errores:
            f.write(error + "\n")


print(f"Log generado: {ruta}")

#Fin de avance 1 por parte de Steve Robinson
'''