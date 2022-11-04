from collections import deque

from src.ply import *
from src.TapiCompi_lex import tokens

from libs.CuboSem import *
from libs.Functions_Directory import Functions_Directory
from libs.Vars_Table import *
from libs.Quadruple import Quadruple

# ----------- Auxiliar variables ------------ #

directory = None  # Variable that stores the directory of functions

scope = None # Variable that stores the current scope
current_type = None # Variable that stores the current type of variables to store
current_var = None # Variable that stores the current variable that is being declared
function_type = None # Variable that stores the type of function that is being declared

quadruples = [] # List that stores the quadruples
quad_pointer = 1; # Variable that stores the number of the next quadruple to be generated

stack_Operators = deque() # Stack that stores the operators ( +, -, *, /, etc. )
stack_Operands = deque() # Stack that stores the operands
stack_Types = deque() # Stack that stores the types of the operands
stack_Jumps = deque() # Stack that stores the jumps


# ----------- Parsing Rules  ----------- #

precedence = (
    ('left', 'OP_EQ', 'OP_NEQ', 'OP_LT', 'OP_GT', 'OP_LTE', 'OP_GTE'),
    ('left', 'OP_ADD', 'OP_SUBTR'),
    ('left', 'OP_MULT', 'OP_DIV'),
    ('left', 'OP_AND', 'OP_OR'),
    ('right', 'OP_ASSIGN'),
)

## -- <programa> --
def p_programa(p):
    '''
    programa : PROGRAM ID create_funcs_dict SEP_COLON aux_prog aux_prog2 MAIN save_func lPAREN rPAREN cuerpo
    '''
    p[0] = "Success"
    
    print('\n')
    print(f'\n {"Cuadruplos:":^50s}')
    print(f' {"~"*50}')        
    global quadruples
    for quad in quadruples:
        if quad != None:
            quad.print()
    
    global directory
    directory.print_Directory()
    print('\n')
        
    for key in directory.Table:
        directory.Table[key].print_VarsTable()
    

def p_aux_prog(p):
    '''aux_prog : dec_var
                | empty'''

def p_aux_prog2(p):
    '''aux_prog2 : dec_func aux_prog2
                 | empty'''


## -- <cuerpo> --
def p_cuerpo(p):
    '''
    cuerpo : lBRACE aux_cuerpo bloque rBRACE
    '''

def p_aux_cuerpo(p):
    '''aux_cuerpo : dec_var
                  | empty'''

## -- <bloque> --
def p_bloque(p):
    '''bloque : estatuto bloque
                | empty'''

## -- <dec_var> --
def p_dec_var(p):
    ' dec_var : VAR aux_dv'

def p_aux_dv(p):
    '''aux_dv : aux_dv2 save_type aux_dv3 SEP_SEMICOLON
                | aux_dv2 save_type aux_dv3 SEP_SEMICOLON aux_dv
    '''
    
def p_aux_dv2 (p):
    '''aux_dv2 : tipo_s
                | tipo_c'''
    p[0] = p[1] # Pass the token to the parent rule
    
def p_aux_dv3(p):
    'aux_dv3 : ID save_var aux_dv4 aux_dv6'

def p_aux_dv4(p):
    '''aux_dv4 : arr aux_dv5
               | empty'''

def p_aux_dv5(p):
    '''aux_dv5 : arr
               | empty'''
               
def p_aux_dv6(p):
    '''aux_dv6 : SEP_COMMA aux_dv3
               | empty'''
               
# -- <tipo_s> --
def p_tipo_s(p):
    '''tipo_s : INT
              | FLOAT
              | CHAR
              | BOOL'''
    p[0] = p[1] # Pass the token to the parent rule


# -- <tipo_c> --
def p_tipo_c(p):
    '''tipo_c : DATAFRAME
              | FILE '''
    p[0] = p[1] # Pass the token to the parent rule


# -- <arr> --
def p_arr(p):
    'arr : lBRACKET aux_arr add_var_dimension rBRACKET'

def p_aux_arr(p):
    '''aux_arr : ID
               | CTE_I'''
    p[0] = p[1] # Pass the token to the parent rule


# -- <call_var> --
def p_call_var(p):
    'call_var : ID aux_cv check_var_exists'
    p[0] = p[1] # Pass the token to the parent rule
    
    global current_type
    current_type = directory.Table[scope].varsTable.Table[p[1]].get_Type()
    
def p_aux_cv(p):
    '''aux_cv : arr aux_cv2
              | empty'''

def p_aux_cv2(p):
    '''aux_cv2 : arr
               | empty'''


# -- <dec_func> --
def p_dec_func(p):
    'dec_func : FUNC aux_df save_func_type ID save_func lPAREN aux_df2 rPAREN cuerpo'
    
def p_aux_df(p):
    '''aux_df : VOID
              | tipo_s'''
    p[0] = p[1] # Pass the token to the parent rule
    
def p_aux_df2(p):
    '''aux_df2 : params
               | empty'''


## -- <params> --
def p_params(p):
    'params : tipo_s save_type ID aux_cv add_param aux_params'

def p_aux_params(p):
    '''aux_params : SEP_COMMA params
                  | empty'''
              

## -- <call_func>
def p_call_func(p):
    'call_func : ID lPAREN aux_cf rPAREN'

def p_aux_cf(p):
    '''aux_cf : h_exp aux_cf2
              | empty'''
              
def p_aux_cf2(p):
    '''aux_cf2 : SEP_COMMA aux_cf
               | empty'''
             
  
## -- <estatuto> --
def p_estatus(p):
    '''estatuto : aux_estatuto SEP_SEMICOLON
                | COMENTARIO'''

def p_aux_estatuto(p):
    '''aux_estatuto : asignacion
                    | call_func
                    | leer
                    | escribir
                    | condicion
                    | ciclo_while
                    | ciclo_for
                    | return'''

## -- <return> --
def p_return(p):
    'return : RETURN lPAREN h_exp rPAREN'
    
    
## -- <asignacion> --
def p_asignacion(p):
    'asignacion : call_var push_operand OP_ASSIGN push_operator h_exp quad_assign' 

  
## -- <leer> --
def p_leer(p):
    'leer : READ lPAREN aux_leer rPAREN'

def p_aux_leer(p):
    '''aux_leer : call_var quad_read
                | call_var quad_read SEP_COMMA aux_leer'''
                
                
## -- <escribir> --
def p_escribir(p):
    'escribir : PRINT lPAREN aux_escribir rPAREN'
    
def p_aux_escribir(p):
    '''aux_escribir : aux_escribir2 
                    | aux_escribir2 SEP_COMMA aux_escribir'''

def p_aux_escribir2(p):
    '''aux_escribir2 : h_exp quad_print_exp
                    | LETRERO quad_print
                    | CTE_CHAR quad_print'''
    p[0] = p[1] # Pass the token to the parent rule
        
                    
## -- <condicion> --
def p_condicion(p):
    'condicion : IF lPAREN h_exp rPAREN bloque aux_condicion'

def p_aux_condicion(p):
    '''aux_condicion : ELSE bloque
                     | empty'''


## -- <ciclo_while> --
def p_ciclo_while(p):
    'ciclo_while : WHILE lPAREN h_exp rPAREN bloque'


## -- <ciclo_for> --
def p_ciclo_for(p):
    'ciclo_for : FOR lPAREN ID OP_ASSIGN h_exp TO h_exp rPAREN aux_ciclofor bloque'

def p_aux_ciclofor(p):
    '''aux_ciclofor : STEP h_exp
                    | empty'''


## -- <h_exp> --
def p_h_exp(p):
    '''h_exp : s_exp
             | s_exp aux_h_exp h_exp'''
             
def p_aux_h_exp(p):
    '''aux_h_exp : OP_AND
                 | OP_OR'''

## -- <s_exp> --
def p_s_exp(p):
    '''s_exp : exp
             | exp aux_s_exp s_exp'''

def p_aux_s_exp(p):
    '''aux_s_exp : OP_EQ
                 | OP_NEQ
                 | OP_GT
                 | OP_LT
                 | OP_GTE
                 | OP_LTE'''

## -- <exp> --
def p_exp(p):
    '''exp : termino
           | termino aux_exp exp'''
           
def p_aux_exp(p):
    '''aux_exp : OP_ADD
               | OP_SUBTR'''

## -- <termino> --
def p_termino(p):
    '''termino : factor 
               | factor OP_MULT push_operator termino
               | factor OP_DIV push_operator termino'''
           
## -- <factor> --  
    #** Falta agregar que factor pueda ser negativo (OP_SUBTR factor)
def p_factor(p):
    '''factor : lPAREN h_exp rPAREN
              | CTE_I type_int push_operand
              | CTE_F type_float push_operand
              | call_var push_operand
              | call_func'''
    

# Error rule for syntax errors
def p_error(p):
    if p == -2:
        print("Syntax error in parsing, exiting compilation ...")
        exit()
    if p:
        print("Error de sintaxis en '%s'" % p.value)
    else:
        print("Error de sintaxis en EOF")
    parser.error = 1
    


def p_empty(p):
    'empty :'
    pass

# ----------- Neuralgic Points ----------- #

def p_create_funcs_dict(p):
    'create_funcs_dict : '
    
    quadruples.append(None) # Add a None to the list so the quadruples list can be indexed from 1
    
    global scope
    scope = 'global'
    
    global directory
    directory = Functions_Directory()
    directory.add_Function(scope, 'void', 0)    
    directory.Table[scope].varsTable.add_Variable(p[-1], 'Program', 0)


def p_save_type(p):
    'save_type : '
    
    global current_type 
    current_type = p[-1]
    

def p_save_var(p):
    'save_var : '
    
    global current_var
    current_var = p[-1]
    
    # Validate that current variable doesnt exist in the current scope
    if (directory.Table[scope].varsTable.check_Existence(current_var)):
        print("Error: Multiple declaration. \n Variable '%s' already exists in scope '%s'" % (current_var, scope))
        p_error(-2)
    else:
        directory.Table[scope].varsTable.add_Variable(current_var, current_type, 0)
    
def p_add_var_dimension(p):
    'add_var_dimension : '
    
    directory.Table[scope].varsTable.add_Var_Dimension(current_var, p[-1])
    
def p_save_func_type(p):
    'save_func_type : '
    
    global function_type
    function_type = p[-1]
    
def p_save_func(p):
    'save_func : '
    
    global scope
    scope = p[-1]
    
    if (directory.check_Existence(scope)):
        print("Error: Function '%s' already exists" % scope)
        p_error(-2)
    else:
        directory.add_Function(scope, function_type, 0)
    
def p_add_param(p):
    'add_param : '
    
    directory.add_Func_Param(scope, current_type)
    directory.Table[scope].varsTable.add_Variable(p[-2], current_type, 0)
    
def p_check_var_exists(p):
    'check_var_exists : '
    
    if (not directory.Table[scope].varsTable.check_Existence(p[-2]) and not directory.Table['global'].varsTable.check_Existence(p[-2])):
        print("Error: Variable '%s' does not exist in scope '%s' nor in global" % (p[-2], scope))
        p_error(-2)
        
def p_type_int(p):
    'type_int : '
    
    global current_type
    current_type = 'int'
    p[0] = p[-1] # Return the value of the constant
    
def p_type_float(p):
    'type_float : '
    
    global current_type
    current_type = 'float'
    p[0] = p[-1] # Return the value of the constant
        
def p_push_operand(p):
    'push_operand : '
    
    global stack_Operands
    global stack_Types
    
    operand = p[-1]
    stack_Operands.append(operand)
    stack_Types.append(current_type)
    
def p_push_operator(p):
    'push_operator : '
    
    global stack_Operators
    stack_Operators.append(p[-1])
    
def p_quad_assign(p):
    'quad_assign : '
    
    global quadruples
    global quad_pointer
    
    operator = stack_Operators.pop()
    oper_Izq = stack_Operands.pop()
    oper_Der = stack_Operands.pop()
    
    type_Izq = stack_Types.pop()
    type_Der = stack_Types.pop()
    if (validate_type(operator,type_Izq, type_Der) == -1):
        print("Error: Operation '%s' with mismatched types '%s' and '%s'" % (operator, type_Izq, type_Der))
        p_error(-2)
        
    quadruples.append(Quadruple(operator, oper_Izq, '', oper_Der))
    quad_pointer += 1
    
def p_quad_read(p):
    'quad_read : '
    
    global quadruples
    global quad_pointer
    
    quadruples.append(Quadruple('READ', '', '', p[-1]))
    quad_pointer += 1

def p_quad_print(p):
    'quad_print : '
    
    global quadruples
    global quad_pointer
    
    quadruples.append(Quadruple('PRINT', '', '', p[-1]))
    quad_pointer += 1
    
def p_quad_print_exp(p):
    'quad_print_exp : '
    
    global stack_Operands
    global stack_Types
    global quadruples
    global quad_pointer
    
    stack_Types.pop() # Pop the type of the expression
    
    quadruples.append(Quadruple('PRINT', '', '', stack_Operands.pop()))
    quad_pointer += 1
    
    # TO DO: If the operand was a temporal, free the used space.
    
    
""" def p_quad_add_substr(p):
    'quad_add_substr : '
    
    global stack_Operands
    global stack_Types
    global stack_Operators
    global quadruples
    global quad_pointer
    
    if (stack_Operands[-1] == '+' | stack_Operands[-1] == '-'): # Check if top of stack is add or subtract pending
        # Take out operands and their types
        right_operand = stack_Operands.pop()
        right_type = stack_Types.pop()
        left_operand = stack_Operands.pop()
        left_type = stack_Types.pop()
        
        operator = stack_Operators.pop()
        
        # Check if types are valid """
# ----------- Methods ----------- #

# Return the parser
parser = yacc.yacc()  


def parse(data, debug=0):
    parser.error = 0
    p = parser.parse(data, debug=debug)
    if parser.error:
        return None
    return p

