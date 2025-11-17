import ply.yacc as yacc
from Analizador_Lexico import tokens
from datetime import datetime
import os
from zoneinfo import ZoneInfo

syntax_errors_list = []

#Tabla de simbolos
symbol_table = {
    "variables":{},
    "types":{
        "String", "Long","Double" , "Boolean"
    }

}

types={
    "Long": "INTEGER",
    "Double": "FLOAT",
    "Boolean": "BOOLEAN",
    "String" : "STRING",
}



#Regla definida por Jefferson Saltos:
def p_programa(p):
    '''programa : sentencia
    | sentencia programa'''

#Regla definida por Jefferson Saltos:
def p_sentencia(p):
    '''sentencia : declaration
    | call_function
    | print_function
    | println_function
    | control_if
    | readline
    | for_loop
    | while_loop
    | function
    | class
    | function_lambda
    | variable_assigment'''

#Regla definida por Jefferson Saltos:
def p_sentencias(p):
    '''sentencias : sentencia 
    | sentencia sentencias'''

#Regla definida por Jefferson Saltos:
def p_declaration(p):
    'declaration : declaration_start IDENTIFIER COLON data_types ASSIGMENT declaration_options'
    name=p[2]
    type=p[4]
    print(p.slice[6].type)
    if name in symbol_table["variables"]:
        print(f"Error Semantico : La siguiente variable {name} ya fue declarada")
    elif p.slice[6].type=="INTEGER" and p[4] != "Long":
        print(f"Error Semantico : La variable {name} y su declaracion difiere en el tipo de dato ")
    elif p.slice[6].type=="FLOAT" and p[4] != "Double":
        print(f"Error Semantico : La variable {name} y su declaracion difiere en el tipo de dato ")
    elif p.slice[6].type=="BOOLEAN" and p[4] != "Boolean":
        print(f"Error Semantico : La variable {name} y su declaracion difiere en el tipo de dato ")
    elif p.slice[6].type=="STRING" and p[4] != "String":
        print(f"Error Semantico : La variable {name} y su declaracion difiere en el tipo de dato ")


    symbol_table["variables"][name]={
        "type" : type,
        "value": p[6] #266
    }
    print(symbol_table)

# var paco : String = pepe



#Regla definida por Jefferson Saltos:
def p_data_types(p):
    '''data_types : IDENTIFIER
    | mutable_map
    | mutable_list '''
    
    if p[1] not in symbol_table["types"]: 
        print(f"Error Semantico : El tipo de dato {p[1]} no existe") 
    else:
        p[0]=p[1]



def p_map_inputs(p):
    '''map_inputs : INTEGER
    | FLOAT
    | STRING
    | call_function
    '''

#Regla definida por Jefferson Saltos: 
def p_declaration_options(p):
    '''declaration_options :  INTEGER
    | FLOAT
    | STRING
    | aritmetic_operation
    | boolean_variable
    | boolean_operation
    | call_function '''
    p.slice[0].type=p.slice[1].type
    p[0]=p[1]


def p_variable_assigment(p):
    ''' variable_assigment : IDENTIFIER ASSIGMENT declaration_options'''

    name=p[1]
    
    print(p.slice[3].type)
    #{'Boolean', 'Long', 'String', 'Double'}}

    if name not in symbol_table["variables"]:
        print(f"Error Semantico : La siguiente variable {name} no ha sido declarada")
    elif p.slice[3].type=="INTEGER" and symbol_table["variables"][p[1]]["type"] != "Long":
        print(f"Error Semantico : La variable {name} y su declaracion difiere en el tipo de dato ")
    elif p.slice[3].type=="FLOAT" and symbol_table["variables"][p[1]]["type"] != "Double":
        print(f"Error Semantico : La variable {name} y su declaracion difiere en el tipo de dato ")
    elif p.slice[3].type=="BOOLEAN" and symbol_table["variables"][p[1]]["type"] != "Boolean":
        print(f"Error Semantico : La variable {name} y su declaracion difiere en el tipo de dato ")
    elif p.slice[3].type=="STRING" and symbol_table["variables"][p[1]]["type"] != "String":
        print(f"Error Semantico : La variable {name} y su declaracion difiere en el tipo de dato ")

    symbol_table["variables"][name]["value"]=p[3]
    print(symbol_table)

#Regla definida por Jefferson Saltos
def p_aritmetic_operation(p):
    '''aritmetic_operation : number_variable operator number_variable
    | aritmetic_operation operator number_variable '''
    
    if p[2]=="-":
        p[0] = p[1] - p[3]
        p.slice[0].type=p.slice[1].type
    elif p[2] == "+":
        p[0] = p[1] + p[3]
        p.slice[0].type=p.slice[1].type
    elif p[2] =="*":
        p[0] = p[1] * p[3]
        p.slice[0].type=p.slice[1].type
    elif p[2]=="/":
        p[0] = p[1] / p[3]
        p.slice[0].type=p.slice[1].type
    elif p[2] == "%":
        p[0]=p[1] % p[3]
        p.slice[0].type=p.slice[1].type

#Regla definida por Jefferson Saltos
def p_number(p):
    '''number : INTEGER
    | FLOAT'''
    p[0]=p[1]
    p.slice[0].type=p.slice[1].type

#Regla definida por Steve Robinson
def p_number_variable(p):
    '''number_variable : INTEGER
    | FLOAT
    | identifier_number   '''
    p[0] = p[1]
    p.slice[0].type=p.slice[1].type
    

def p_identifier_number(p):
    ''' identifier_number : IDENTIFIER'''
    if p[1] not in symbol_table["variables"]:
        print(f"Error Semantico: La variable {p[1]} no existe")
    else :
        p[0] = symbol_table["variables"][p[1]]["value"]
        p.slice[0].type= types[symbol_table["variables"][p[1]]["type"]] #"Long"

#Regla definida por Jefferson Saltos
def p_operator(p):
    '''operator : MINUS
    | PLUS
    | TIMES
    | DIVIDE
    | MOD'''
    p[0]=p[1]


#Regla definida por Jefferson Saltos
def p_boolean_operation(p):
    '''boolean_operation : boolean_variable logical_operator boolean_variable
    | boolean_operation logical_operator boolean_variable'''
    if p[2]=="&&":
        p[0] = p[1] and p[3]
        p.slice[0].type=p.slice[1].type
        print(p[0])
    elif p[2] == "||":
        p[0] = p[1] or p[3]
        p.slice[0].type=p.slice[1].type
    

#Regla definida por Jefferson Saltos
def p_logical_operator(p):
    '''logical_operator : AND
    | OR
    '''
    p[0]=p[1]
    p.slice[0].type=p.slice[1].type

#Regla definida por Jefferson Saltos
def p_boolean_variable(p):
    '''boolean_variable : identifier_boolean
    | BOOLEAN
    | comparison_operation
    | boolean_variable_not'''
    if p[1]=="true" or p[1]==True:
        p[0]=True
    elif p[1]=="false" or p[1]==False:
        p[0]=False
    p.slice[0].type=p.slice[1].type
    

def p_boolean_variable_not(p):
    '''boolean_variable_not : NOT boolean_variable'''
    if p[2]=="true" or p[2]==True:
        p[0]=False
    elif p[2]=="false" or p[2]==False:
        p[0]=True
    p.slice[0].type=p.slice[2].type


def p_identifier_boolean(p):
    ''' identifier_boolean : IDENTIFIER'''
    if p[1] not in symbol_table["variables"]:
        print(f"Error Semantico: La variable {p[1]} no existe")
    p[0] = symbol_table["variables"][p[1]]["value"]
    p.slice[0].type= types[symbol_table["variables"][p[1]]["type"]] 

#Regla definida por Jefferson Saltos
def p_comparison_operation(p):
    '''comparison_operation : comparison_variable comparison_operator comparison_variable '''
    if p[2]==">":
        p[0] = p[1] > p[3]
        p.slice[0].type="Boolean"
    elif p[2] == "<":
        p[0] = p[1] < p[3]
        p.slice[0].type="Boolean"
    elif p[2] =="==":
        p[0] = p[1] == p[3]
        p.slice[0].type="Boolean"
    elif p[2]==">=":
        p[0] = p[1] >= p[3]
        p.slice[0].type="Boolean"
    elif p[2] == "<=":
        p[0]=p[1] <= p[3]
        p.slice[0].type="Boolean"
    elif p[2] == ">=":
        p[0]=p[1] >= p[3]
        p.slice[0].type="Boolean"
        

#Regla definida por Jefferson Saltos
def p_comparison_variable(p):
    '''comparison_variable : identifier_comparison
    | number
    | STRING
    | aritmetic_operation'''
    p[0]=p[1]
    p.slice[0].type=p.slice[1].type


def p_identifier_comparison(p):
    ''' identifier_comparison : IDENTIFIER'''
    if p[1] not in symbol_table["variables"]:
        print(f"Error Semantico: La variable {p[1]} no existe")
    p[0] = symbol_table["variables"][p[1]]["value"]
    p.slice[0].type= types[symbol_table["variables"][p[1]]["type"]] 
    

#Regla definida por Jefferson Saltos
def p_comparison_operator(p):
    '''comparison_operator : GREATER_THAN
    | LESS_THAN
    | GREATER_OR_EQUAL
    | LESS_OR_EQUAL
    | EQUALS_TO
    | NOT_EQUALS'''
    p[0]=p[1]
    


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
    | mutable_map_parameter
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
def p_mutable_map_parameter(p):
    '''mutable_map_parameter : map_inputs TO map_inputs COMMA map_inputs TO map_inputs'''

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
    '''control_if_input : boolean_operation'''

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

#Regla definida por Jefferson Saltos
def p_function_lambda(p):
    'function_lambda : declaration_start IDENTIFIER COLON LPAREN function_lambda_type RPAREN MINUS GREATER_THAN IDENTIFIER ASSIGMENT LBRACE parameters MINUS GREATER_THAN statements_function_lambda_block RBRACE'

def p_function_lambda_type(p):
    '''function_lambda_type : data_types
    | function_lambda_type COMMA data_types
    | empty'''

#Regla definida por Steve Robinson
def p_statements_function_lambda_block(p):
    '''statements_function_lambda_block :  options_function_lambda_block
    | statements_function_lambda_block options_function_lambda_block'''

#Regla definida por Jefferson Saltos
def p_options_function_lambda_block(p):
    '''options_function_lambda_block : readline
    | control_if
    | for_loop
    | while_loop
    | declaration
    | call_function
    | print_function
    | println_function
    | aritmetic_operation
    | boolean_operation
    | variable_assigment
    '''

#Regla definida por Steve Robinson
def p_parameters(p):
    '''parameters :  IDENTIFIER COLON IDENTIFIER
    | parameters COMMA IDENTIFIER COLON IDENTIFIER
    | empty'''

#Regla definida por Steve Robinson
def p_return_statements(p):
    '''return_statements : RETURN returnables'''

#Regla definida por Steve Robinson
def p_returnables(p):
    '''returnables : declaration_options 
    | empty
    '''

#Regla definida por Steve Robinson
def p_options_function_block(p):
    '''options_function_block : return_statements
    | control_if_function
    | for_loop_function
    | while_loop_function
    | declaration
    | call_function
    | print_function
    | println_function
    | readline
    | function
    | class
    | function_lambda
    | variable_assigment'''

#Regla definida por Steve Robinson
def p_control_if_function(p):
    '''control_if_function : IF LPAREN control_if_input RPAREN LBRACE statements_function_block RBRACE
    | IF LPAREN control_if_input RPAREN LBRACE statements_function_block RBRACE ELSE LBRACE statements_function_block RBRACE
    | IF LPAREN control_if_input RPAREN LBRACE statements_function_block RBRACE control_else_if_function
    | IF LPAREN control_if_input RPAREN LBRACE statements_function_block RBRACE control_else_if_function ELSE LBRACE statements_function_block RBRACE'''

#Regla definida por Steve Robinson
def p_control_else_if_function(p):
    '''control_else_if_function : ELSE IF LPAREN control_if_input RPAREN LBRACE statements_function_block RBRACE
    | control_else_if_function ELSE IF LPAREN control_if_input RPAREN LBRACE statements_function_block RBRACE'''

#Regla definida por Steve Robinson
def p_for_loop_function(p):
    '''for_loop_function : FOR LPAREN for_content RPAREN LBRACE statements_function_block RBRACE'''

#Regla definida por Steve Robinson
def p_while_loop_function(p):
    '''while_loop_function : WHILE LPAREN control_if_input RPAREN LBRACE statements_function_block RBRACE'''

#Regla definida por Steve Robinson
def p_statements_function_block(p):
    '''statements_function_block :  options_function_block
    | statements_function_block options_function_block'''

#Regla definida por Steve Robinson
def p_class(p):
    '''class : CLASS IDENTIFIER LPAREN atributes RPAREN class_post_atributes'''

#Regla definida por Steve Robinson
def p_class_statement(p):
    '''class_statement :  declaration
    | function
    | function_lambda'''

#Regla definida por Steve Robinson
def p_class_statements(p):
    """class_statements : class_statement 
    | class_statements class_statement"""

#Regla definida por Steve Robinson
def p_class_post_atributes(p):
    """class_post_atributes : LBRACE class_statements RBRACE
    | empty"""

#Regla definida por Steve Robinson
def p_atributes(p):
    '''atributes : declaration_start IDENTIFIER COLON IDENTIFIER
    | atributes COMMA declaration_start IDENTIFIER COLON IDENTIFIER
    | empty'''

def p_declaration_start(p):
    """declaration_start : VAL
    | VAR"""

#Regla definida por Jefferson Saltos
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    if p:
        mensaje = f"Error sintáctico en la línea {p.lineno}: Token inesperado '{p.value}' (Tipo: {p.type})"
    else:
        mensaje = "Error sintáctico: Fin de archivo inesperado (EOF)"
    print(mensaje)
    syntax_errors_list.append(mensaje)

# Build the parser
parser = yacc.yacc()

#val sum: (Int, Int) -> Int = { x: Int, y: Int -> x + y }
"""
while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)

"""



usuario_git = "rsaltos04"
ecuador_tz = ZoneInfo("America/Guayaquil")
ahora = datetime.now(ecuador_tz)
nombre_archivo = f"sintactico-{usuario_git}-{ahora.strftime('%d-%m-%Y-%Hh%M')}.txt"
ruta = f"logs/{nombre_archivo}"
input_file_path = 'algoritmos/HelloWorld.kt'

os.makedirs(os.path.dirname(ruta), exist_ok=True)
log_content = []

log_content.append("--- LOG DE ANÁLISIS SINTÁCTICO ---")
log_content.append(f"Fecha: {ahora.strftime('%d/%m/%Y %H:%M:%S')}")
log_content.append(f"Usuario: {usuario_git}")
log_content.append(f"Archivo Analizado: {input_file_path}")
log_content.append("-" * 40)

syntax_errors_list.clear()

try:
    with open(input_file_path, 'r') as file:
        all_lines = file.readlines()
        data = "".join(all_lines)
    
    result = parser.parse(data)
        
    if syntax_errors_list:
        log_content.append("\n--- Errores Sintácticos ---")
        for error in syntax_errors_list:
            log_content.append(f"- {error}")
    else:
        log_content.append(f"No hay errores sintácticos")

except FileNotFoundError:
    log_content.append("ESTADO: FALLIDO")
    log_content.append(f"ERROR CRÍTICO: No se pudo encontrar el archivo de entrada en '{input_file_path}'.")

"""
except Exception as e:
    log_content.append("ESTADO: FALLIDO (Error Inesperado del Script)")
    log_content.append(f"\n--- Mensaje de Error ---")
    log_content.append(str(e))
"""
    



try:
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("\n".join(log_content))
    
    print(f"Log guardado exitosamente en: {ruta}")

except IOError as io_e:
    print(f"Error CRÍTICO: No se pudo escribir el archivo log en '{ruta}'.")
    print(f"Detalle: {io_e}")

