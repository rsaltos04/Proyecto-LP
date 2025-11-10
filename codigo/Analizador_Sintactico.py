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
    | control_if
    | readline
    | for_loop
    | while_loop
    | function
    | class'''

#Regla definida por Jefferson Saltos:
def p_sentencias(p):
    '''sentencias : sentencia 
    | sentencia sentencias'''

#Regla definida por Jefferson Saltos:
def p_declaration_var(p):
    'declaration_var : VAR IDENTIFIER COLON data_types ASSIGMENT declaration_options'

#Regla definida por Jefferson Saltos:
def p_data_types(p):
    '''data_types : IDENTIFIER
    | mutable_map
    | mutable_list '''

#Regla definida por Jefferson Saltos:
def p_declaration_options(p):
    '''declaration_options :  INTEGER
    | FLOAT
    | STRING
    | BOOLEAN'''

#Regla definida por Jefferson Saltos
def p_declaration_val(p):
    'declaration_val : VAL IDENTIFIER COLON data_types ASSIGMENT declaration_options'

#Regla definida por Jefferson Saltos
def p_aritmetic_operation(p):
    '''aritmetic_operation : number_variable operator number_variable
    | aritmetic_operation operator number_variable '''

#Regla definida por Jefferson Saltos
def p_number(p):
    '''number : INTEGER
    | FLOAT'''

#Regla definida por Steve Robinson
def p_number_variable(p):
    '''number_variable : INTEGER
    | FLOAT
    | IDENTIFIER   '''

#Regla definida por Jefferson Saltos
def p_operator(p):
    '''operator : MINUS
    | PLUS
    | TIMES
    | DIVIDE
    | MOD'''


#Regla definida por Jefferson Saltos
def p_boolean_operation(p):
    '''boolean_operation : boolean_variable logical_operator boolean_variable
    | boolean_operation logical_operator boolean_variable'''

#Regla definida por Jefferson Saltos
def p_logical_operator(p):
    '''logical_operator : AND
    | OR
    '''

#Regla definida por Jefferson Saltos
def p_boolean_variable(p):
    '''boolean_variable : IDENTIFIER
    | BOOLEAN
    | comparison_operation
    | NOT boolean_variable'''

#Regla definida por Jefferson Saltos
def p_comparison_operation(p):
    '''comparison_operation : comparison_variable comparison_operator comparison_variable '''

#Regla definida por Jefferson Saltos
def p_comparison_variable(p):
    '''comparison_variable : IDENTIFIER
    | number
    | STRING
    | aritmetic_operation'''

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

#Regla definida por Steve Robinson
def p_mutable_list(p):
    'mutable_list : MUTABLE_LIST LESS_THAN generic GREATER_THAN'

#Regla definida por Jefferson Saltos
def p_generic(p):
    '''generic : data_types'''

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
    | boolean_operation'''

#Regla definida por Steve Robinson
def p_readline(p):
    '''readline : READLN LPAREN RPAREN'''

#Regla definida por Steve Robinson
def p_for_loop(p):
    '''for_loop : FOR LPAREN for_content RPAREN LBRACE options_control_block RBRACE'''

#Regla definida por Steve Robinson
def p_for_content(p):
    '''for_content : IDENTIFIER IN INTEGER RANGE INTEGER
    | IDENTIFIER IN IDENTIFIER'''

#Regla definida por Steve Robinson
def p_while_loop(p):
    '''while_loop : WHILE LPAREN control_if_input RPAREN LBRACE options_control_block RBRACE'''

#Regla definida por Steve Robinson
def p_function(p):
    '''function : FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements_function_block RBRACE'''

#Regla definida por Steve Robinson
def p_parameters(p):
    '''parameters :  IDENTIFIER COLON IDENTIFIER
    | parameters COMMA IDENTIFIER COLON IDENTIFIER
    | empty'''

#Regla definida por Steve Robinson
def p_return_statements(p):
    '''return_statements : RETURN
    | RETURN declaration_options
    | RETURN IDENTIFIER
    | RETURN aritmetic_operation
    | RETURN boolean_operation
    | RETURN call_function'''

#Regla definida por Steve Robinson
def p_options_function_block(p):
    '''options_function_block : sentencia 
    | return_statements
    | empty'''

#Regla definida por Steve Robinson
def p_statements_function_block(p):
    '''statements_function_block :  options_function_block
    | statements_function_block options_function_block'''

#Regla definida por Steve Robinson
def p_class(p):
    '''class : class_declaration'''

#Regla definida por Steve Robinson
def p_class_declaration(p):
    '''class_declaration :  CLASS IDENTIFIER LPAREN parameters RPAREN LBRACE class_statements RBRACE'''

#Regla definida por Steve Robinso
def p_class_statements(p):
    '''class_statements :  declaration_var 
    | declaration_val
    | function'''

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

