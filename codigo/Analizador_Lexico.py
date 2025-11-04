import ply.lex as lex

# Inicio del avance 1 por parte de Jefferson Saltos
reserved = {
   "fun": "FUNCTION",
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'for' : 'FOR',
   'val' : 'VAL',
   'var' : 'VAR',
   'Long': 'LONG',
   'Double': 'DOUBLE',
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
   'VARIABLE',
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
   "COMMENT_MULTIPLE_LINES"

) + tuple(reserved.values())

# Regular expression rules for simple tokens
t_COLON= r':'
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
t_COMMENT_ONE_LINE=r'\/\/[\w ]*'
t_COMMENT_MULTIPLE_LINES=r'\/\*(.|\s)*\*\/'



def t_MUTABLE_LIST(t):
    r'MutableList<.+>'
    return t

def t_MUTABLE_LIST_ERROR(t):
    r'MutableList<\s*>|MutableList<>|MutableList\s*<|MutableList[^<]'
    print(f"Error léxico: MutableList mal formado '{t.value}' en línea {t.lineno}, posición {t.lexpos}")
    
#Fin de avance 1 por parte de Jefferson Saltos