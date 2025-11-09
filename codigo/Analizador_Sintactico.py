import ply.yacc as yacc
from Analizador_Lexico import tokens

#Regla definida por Jefferson Saltos:
def p_programa(p):
    '''programa : sentencia 
    | sentencia programa'''

#Regla definida por Jefferson Saltos:
def p_sentencia(p):
    '''sentencia : declaration_var 
    | declaration_val
    | aritmetic_operation
    | boolean_operation
    | comparison_operation
    | call_function
    | print_function
    | println_function
    | mutable_map
    | control_if'''

#Regla definida por Jefferson Saltos:
def p_sentencias(p):
    '''sentencias : sentencia 
    | sentencia sentencias'''

#Regla definida por Jefferson Saltos:
def p_declaration_var(p):
    'declaration_var : VAR IDENTIFIER COLON data_types ASSIGMENT declaration_options '

#Regla definida por Jefferson Saltos:
def p_data_types(p):
    'data_types : IDENTIFIER'

#Regla definida por Jefferson Saltos:
def p_declaration_options(p):
    '''declaration_options :  INTEGER
    | FLOAT
    | STRING
    | BOOLEAN'''

#Regla definida por Jefferson Saltos
def p_declaration_val(p):
    'declaration_val : VAL IDENTIFIER COLON data_types ASSIGMENT declaration_options '

#Regla definida por Jefferson Saltos
def p_aritmetic_operation(p):
    '''aritmetic_operation : number operator number
    | aritmetic_operation operator number '''

#Regla definida por Jefferson Saltos
def p_number(p):
    '''number : INTEGER
    | FLOAT'''

#Regla definida por Jefferson Saltos
def p_operator(p):
    '''operator : MINUS
    | PLUS
    | TIMES
    | DIVIDE
    | MOD'''


#Regla definida por Jefferson Saltos
def p_boolean_operation(p):
    '''boolean_operation : optional_boolean_operator boolean_variable logical_operator optional_boolean_operator boolean_variable
    | boolean_operation logical_operator optional_boolean_operator boolean_variable'''

#Regla definida por Jefferson Saltos
def p_logical_operator(p):
    '''logical_operator : AND
    | OR
    '''

#Regla definida por Jefferson Saltos
def p_optional_boolean_operator(p):
    '''optional_boolean_operator : NOT
    | empty'''

#Regla definida por Jefferson Saltos
def p_boolean_variable(p):
    '''boolean_variable : IDENTIFIER
    | BOOLEAN'''

#Regla definida por Jefferson Saltos
def p_comparison_operation(p):
    'comparison_operation : comparison_variable comparison_operator comparison_variable '

#Regla definida por Jefferson Saltos
def p_comparison_variable(p):
    '''comparison_variable : IDENTIFIER
    | number
    | STRING'''

#Regla definida por Jefferson Saltos
def p_comparison_operator(p):
    '''comparison_operator : GREATER_THAN
    | LESS_THAN
    | GREATER_OR_EQUAL
    | LESS_OR_EQUAL
    | EQUALS_TO
    | NOT_EQUALS'''


#Regla definida por Jefferson Saltos
def p_call_function(p):
    'call_function : IDENTIFIER LPAREN function_input RPAREN'

#Regla definida por Jefferson Saltos
def p_function_input(p):
    '''function_input : function_input_options
    | function_input COMMA function_input_options'''

#Regla definida por Jefferson Saltos
def p_function_input_options(p):
    '''function_input_options : number
    | IDENTIFIER
    | STRING
    | empty
    '''

#Regla definida por Jefferson Saltos
def p_print_function(p):
    'print_function : PRINT LPAREN function_input RPAREN'

#Regla definida por Jefferson Saltos
def p_println_function(p):
    'println_function : PRINTLN LPAREN function_input RPAREN'

#Regla definida por Jefferson Saltos
def p_mutable_map(p):
    'mutable_map : MUTABLE_MAP LESS_THAN generic COMMA generic GREATER_THAN'

#Regla definida por Jefferson Saltos
def p_generic(p):
    '''generic : data_types 
    | mutable_map'''

#Regla definida por Jefferson Saltos
def p_control_if(p):
    '''control_if : IF LPAREN control_if_input RPAREN LBRACE options_control_block RBRACE
    | IF LPAREN control_if_input RPAREN LBRACE options_control_block RBRACE ELSE LBRACE options_control_block RBRACE
    | IF LPAREN control_if_input RPAREN LBRACE options_control_block RBRACE control_else_if
    | IF LPAREN control_if_input RPAREN LBRACE options_control_block RBRACE control_else_if ELSE LBRACE options_control_block RBRACE'''

#Regla definida por Jefferson Saltos
def p_options_control_block(p):
    '''options_control_block : empty
    | sentencias'''

#Regla definida por Jefferson Saltos
def p_control_else_if(p):
    '''control_else_if : ELSE IF LPAREN control_if_input RPAREN LBRACE options_control_block RBRACE
    | control_else_if ELSE IF LPAREN control_if_input RPAREN LBRACE options_control_block RBRACE'''

#Regla definida por Jefferson Saltos
def p_control_if_input(p):
    '''control_if_input : boolean_variable
    | comparison_operation
    | boolean_operation'''

#Regla definida por Jefferson Saltos
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)

