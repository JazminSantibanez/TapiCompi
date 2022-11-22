from collections import deque

from src.ply import *
from src.TapiCompi_lex import tokens

import libs.CuboSem as CuboSem
#from libs.CuboSem import *
from libs.Functions_Directory import Functions_Directory
from libs.Vars_Table import Vars_Table, Var_Info
from libs.Quadruple import Quadruple
from libs.Address_Manager import Address_Manager


# ----------- Auxiliar variables ------------ #

directory = Functions_Directory()  # Variable that stores the directory of functions
const_table = dict() # Dictionary that stores the constants. {Key: Number/Char, Value: Address}

scope = None # Variable that stores the current scope
func = None # Variable that stores the name of the func called
current_type = None # Variable that stores the current type of variables to store
current_var = None # Variable that stores the current variable that is being declared
function_type = None # Variable that stores the type of function that is being declared

quadruples = [] # List that stores the quadruples
quad_pointer = 1; # Variable that stores the number of the next quadruple to be generated

stack_Operators = deque() # Stack that stores the operators ( +, -, *, /, etc. )
stack_Operands = deque() # Stack that stores the operands
stack_Types = deque() # Stack that stores the types of the operands
stack_Jumps = deque() # Stack that stores the jumps

param_counter = 0; # Variable that manages the index of the parameter being analyzed

Addr_Manager = Address_Manager()

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
    programa : PROGRAM ID n_create_funcs_dict SEP_COLON aux_prog aux_prog2 MAIN n_save_func lPAREN rPAREN cuerpo
    '''
    p[0] = "Success"
    
    #directory.Table['global'].print_VarsTable()

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
    '''aux_dv : aux_dv2 n_save_type aux_dv3 SEP_SEMICOLON
                | aux_dv2 n_save_type aux_dv3 SEP_SEMICOLON aux_dv
    '''
    
def p_aux_dv2 (p):
    '''aux_dv2 : tipo_s
                | tipo_c'''
    p[0] = p[1] # Pass the token to the parent rule
    
def p_aux_dv3(p):
    'aux_dv3 : ID n_save_var aux_dv4 aux_dv6'

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
    'arr : lBRACKET aux_arr n_add_var_dimension rBRACKET'

def p_aux_arr(p):
    '''aux_arr : CTE_I'''
    p[0] = p[1] # Pass the token to the parent rule


# -- <call_var> --
def p_call_var(p):
    'call_var : ID aux_cv n_check_var_exists'
   
    global current_type
    if (directory.Table[scope].varsTable.check_Existence(p[1])):
        current_type = directory.Table[scope].varsTable.Table[p[1]].get_Type()
        addr = directory.Table[scope].varsTable.Table[p[1]].get_DirV()
    elif (directory.Table['global'].varsTable.check_Existence(p[1])):
        current_type = directory.Table['global'].varsTable.Table[p[1]].get_Type()
        addr = directory.Table['global'].varsTable.Table[p[1]].get_DirV()
        
    p[0] = addr # Pass the addrs of the variable to the parent rule
    
def p_aux_cv(p):
    '''aux_cv : arr aux_cv2
              | empty'''

def p_aux_cv2(p):
    '''aux_cv2 : arr
               | empty'''


# -- <dec_func> --
def p_dec_func(p):
    'dec_func : FUNC aux_df n_save_func_type ID n_save_func lPAREN aux_df2 rPAREN n_func_start cuerpo n_quad_endfunc'
    # Reset variables address
    Addr_Manager.reset_local()
    
    # Reset the operators, operands and types stacks
    stack_Operators.clear()
    stack_Operands.clear()
    stack_Types.clear()
    
def p_aux_df(p):
    '''aux_df : VOID
              | tipo_s'''
    p[0] = p[1] # Pass the token to the parent rule
    
def p_aux_df2(p):
    '''aux_df2 : params
               | empty'''


## -- <params> --
def p_params(p):
    'params : tipo_s n_save_type ID aux_cv n_add_param aux_params'

def p_aux_params(p):
    '''aux_params : SEP_COMMA params
                  | empty'''
              

## -- <call_func>
def p_call_func(p):
    'call_func : ID n_quad_func_era lPAREN n_false_bottom_start aux_cf n_func_check_params rPAREN n_false_bottom_end n_quad_func_gosub'

def p_aux_cf(p):
    '''aux_cf : h_exp n_quad_func_param aux_cf2
              | empty'''
              
def p_aux_cf2(p):
    '''aux_cf2 : SEP_COMMA aux_cf
               | empty'''
             
  
## -- <estatuto> --
def p_estatuto(p):
    '''estatuto : asignacion
                | call_func
                | leer
                | escribir
                | return
                | condicion
                | ciclo_while
                | ciclo_do_while
                | ciclo_for
                | COMENTARIO'''

## -- <return> --
def p_return(p):
    'return : RETURN lPAREN h_exp rPAREN n_quad_return'
    
    
## -- <asignacion> --
def p_asignacion(p):
    'asignacion : call_var n_push_operand OP_ASSIGN n_push_operator h_exp n_quad_assign' 

  
## -- <leer> --
def p_leer(p):
    'leer : READ lPAREN aux_leer rPAREN'

def p_aux_leer(p):
    '''aux_leer : call_var n_quad_read
                | call_var n_quad_read SEP_COMMA aux_leer'''
                
                
## -- <escribir> --
def p_escribir(p):
    'escribir : PRINT lPAREN aux_escribir rPAREN'
    
def p_aux_escribir(p):
    '''aux_escribir : aux_escribir2 
                    | aux_escribir2 SEP_COMMA aux_escribir'''

def p_aux_escribir2(p):
    '''aux_escribir2 : h_exp n_quad_print_exp
                    | LETRERO n_quad_print
                    | CTE_CHAR n_quad_print'''
    p[0] = p[1] # Pass the token to the parent rule
        
                    
## -- <condicion> --
def p_condicion(p):
    'condicion : IF lPAREN h_exp rPAREN lBRACE n_quad_if_jump_false bloque rBRACE aux_condicion n_quad_if_end'

def p_aux_condicion(p):
    '''aux_condicion : n_quad_if_else ELSE lBRACE bloque rBRACE
                     | empty'''


## -- <ciclo_while> --
def p_ciclo_while(p):
    'ciclo_while : WHILE n_while_exp lPAREN h_exp rPAREN n_quad_while_false lBRACE bloque rBRACE n_quad_while_repeat'

## -- <ciclo_do_while> --
def p_ciclo_do_while(p):
    'ciclo_do_while : DO n_do_while_start lBRACE bloque rBRACE WHILE lPAREN h_exp rPAREN n_quad_do_while_true'

## -- <ciclo_for> --
def p_ciclo_for(p):
    'ciclo_for : FOR lPAREN ID OP_ASSIGN h_exp TO h_exp rPAREN aux_ciclofor bloque'

def p_aux_ciclofor(p):
    '''aux_ciclofor : STEP h_exp
                    | empty'''


## -- <h_exp> --
def p_h_exp(p):
    '''h_exp : s_exp n_quad_and_or
             | s_exp n_quad_and_or aux_h_exp n_push_operator h_exp'''
             
def p_aux_h_exp(p):
    '''aux_h_exp : OP_AND
                 | OP_OR'''
    p[0] = p[1] # Pass the token to the parent rule

## -- <s_exp> --
def p_s_exp(p):
    '''s_exp : exp n_quad_compare
             | exp n_quad_compare aux_s_exp n_push_operator s_exp'''

def p_aux_s_exp(p):
    '''aux_s_exp : OP_EQ
                 | OP_NEQ
                 | OP_GT
                 | OP_LT
                 | OP_GTE
                 | OP_LTE'''
    p[0] = p[1] # Pass the token to the parent rule

## -- <exp> --
def p_exp(p):
    '''exp : termino n_quad_add_substr
           | termino n_quad_add_substr aux_exp exp'''
           
def p_aux_exp(p):
    '''aux_exp : OP_ADD n_push_operator
               | OP_SUBTR n_push_operator'''

## -- <termino> --
def p_termino(p):
    '''termino : factor n_quad_mult_div
               | factor n_quad_mult_div OP_MULT n_push_operator termino
               | factor n_quad_mult_div OP_DIV n_push_operator termino'''
           
## -- <factor> --  
    #** Falta agregar que factor pueda ser negativo (OP_SUBTR factor)
def p_factor(p):
    '''factor : lPAREN n_false_bottom_start h_exp rPAREN n_false_bottom_end
              | CTE_I n_save_cteI n_push_operand
              | CTE_F n_save_cteF n_push_operand
              | call_var n_push_operand
              | call_func'''
    
def p_empty(p):
    'empty :'
    pass

# ----------- Neuralgic Points ----------- #

def p_n_create_funcs_dict(p):
    'n_create_funcs_dict : '
    
    global quad_pointer
    quadruples.append(None) # Add a None to the list so the quadruples list can be indexed from 1
    quadruples.append(Quadruple('GOTO', '', '', 'main')) # Add the first quadruple to the list
    quad_pointer += 1 
    stack_Jumps.append(quad_pointer - 1) 
    
    global scope
    scope = 'global'
    
    global directory
    directory.add_Function(scope, 'void', 0)    
    directory.Table[scope].add_Variable(p[-1], 'Program', 0)


def p_n_save_type(p):
    'n_save_type : '
    
    global current_type 
    current_type = p[-1]
    

def p_n_save_var(p):
    'n_save_var : '
    
    global current_var
    current_var = p[-1]
    
    # Validate that current variable doesnt exist in the current scope
    if (directory.Table[scope].varsTable.check_Existence(current_var)):
        print("Error: Multiple declaration. \n Variable '%s' already exists in scope '%s'" % (current_var, scope))
        p_error(-2)
    
    if (scope == 'global'):
        addr = Addr_Manager.get_Global_Dir(current_type)
    else:
        addr = Addr_Manager.get_Local_Dir(current_type)
    
    #print(scope, current_var, current_type, addr)
    directory.Table[scope].add_Variable(current_var, current_type, addr)
    
def p_n_add_var_dimension(p):
    'n_add_var_dimension : '
    
    directory.Table[scope].varsTable.add_Var_Dimension(current_var, p[-1])
    
def p_n_save_func_type(p):
    'n_save_func_type : '
    
    global function_type
    function_type = p[-1]
    
def p_n_save_func(p):
    'n_save_func : '
    
    global scope
    global function_type
    scope = p[-1]
    
    if (directory.check_Existence(scope)):
        print("Error: Function '%s' already exists" % scope)
        p_error(-2)
    
    if (scope == 'main'):
        quad_goto_main = stack_Jumps.pop()
        quadruples[quad_goto_main].set_Result(quad_pointer)
        
        scope = 'global'
        function_type = 'void'
    else:
        directory.add_Function(scope, function_type, 0)
    
    # If theres a return type, add a variable with the function's name,
    # to store the return value
    
    if (function_type != 'void'):
        if ( directory.Table['global'].varsTable.check_Existence(scope) == False):
            addr = Addr_Manager.get_Global_Dir(function_type)
            directory.Table['global'].add_Variable(scope, function_type, addr)
        else:
            print("Error: A global variable and a function can't share the same ID. \n ID in conflict: '%s'" % (scope))
    
def p_n_add_param(p):
    'n_add_param : '
    
    directory.add_Func_Param(scope, current_type)
    addr = Addr_Manager.get_Local_Dir(current_type)
    directory.Table[scope].add_Variable(p[-2], current_type, addr)
    
    
def p_n_check_var_exists(p):
    'n_check_var_exists : '
    
    if (not directory.Table[scope].varsTable.check_Existence(p[-2]) and not directory.Table['global'].varsTable.check_Existence(p[-2])):
        print("Error: Variable '%s' does not exist in scope '%s' nor in global" % (p[-2], scope))
        p_error(-2)

def p_n_save_cteF(p):
    'n_save_cteF : '
    
    global current_type
    current_type = 'float'
    
    value = p[-1]
    if value in const_table:
        addr = const_table[value]
    else:
        addr = Addr_Manager.get_Const_Float_Dir()
        const_table[p[-1]] = addr
    p[0] = addr # Return the value of the constant
    
def p_n_save_cteI(p):
    'n_save_cteI : '
    
    global current_type
    current_type = 'int'
    
    value = p[-1]
    if value in const_table:
        addr = const_table[value]
    else:
        addr = Addr_Manager.get_Const_Int_Dir()
        const_table[p[-1]] = addr
    p[0] = addr # Return the value of the constant
        
def p_n_push_operand(p):
    'n_push_operand : '
    
    global stack_Operands
    global stack_Types
    
    operand = p[-1]
    stack_Operands.append(operand)
    stack_Types.append(current_type)
    
def p_n_push_operator(p):
    'n_push_operator : '
    
    global stack_Operators
    stack_Operators.append(p[-1])
    
def p_n_quad_assign(p):
    'n_quad_assign : '
    
    global quadruples
    global quad_pointer
    
    operator = stack_Operators.pop()
    oper_Izq = stack_Operands.pop()
    oper_Der = stack_Operands.pop()
    
    type_Izq = stack_Types.pop()
    type_Der = stack_Types.pop()
    if (CuboSem.validate_type(operator,type_Izq, type_Der) == -1):
        print("Error: Operation '%s' with mismatched types '%s' and '%s'" % (operator, type_Izq, type_Der))
        p_error(-2)
        
    quadruples.append(Quadruple(operator, oper_Izq, '', oper_Der))
    quad_pointer += 1
    
def p_n_quad_read(p):
    'n_quad_read : '
    
    global quadruples
    global quad_pointer
    
    quadruples.append(Quadruple('READ', '', '', p[-1]))
    quad_pointer += 1

def p_n_quad_print(p):
    'n_quad_print : '
    
    global quadruples
    global quad_pointer
    
    quadruples.append(Quadruple('PRINT', '', '', p[-1]))
    quad_pointer += 1
    
def p_n_quad_print_exp(p):
    'n_quad_print_exp : '
    
    global stack_Operands
    global stack_Types
    global quadruples
    global quad_pointer
    
    stack_Types.pop() # Pop the type of the expression
    
    quadruples.append(Quadruple('PRINT', '', '', stack_Operands.pop()))
    quad_pointer += 1
    
    # TO DO: If the operand was a temporal, free the used space.
    
    
def p_n_quad_add_substr(p):
    'n_quad_add_substr : '
    
    global stack_Operands
    global stack_Types
    global stack_Operators
    global quadruples
    global quad_pointer
            
    if (len(stack_Operators) > 0 and (stack_Operators[-1] == '+' or stack_Operators[-1] == '-')):
            # Take out operands and their types
            right_operand = stack_Operands.pop()
            right_type = stack_Types.pop()
            left_operand = stack_Operands.pop()
            left_type = stack_Types.pop()
            
            operator = stack_Operators.pop()
            
            # Check if types are valid
            result_type = CuboSem.validate_type(operator, left_type, right_type)
            
            if (result_type == -1):
                print("Error: Operation '%s' with mismatched types '%s' and '%s'" % (operator, left_type, right_type))
                p_error(-2)
                
            #If theres no error: Create a temporal and add the quadruple
            result = Addr_Manager.get_Local_Temporal_Dir(result_type)
            directory.Table[scope].add_Temp(result_type)
            
            # Create quadruple
            quadruples.append(Quadruple(operator, left_operand, right_operand, result))
            quad_pointer += 1
            stack_Operands.append(result)
            stack_Types.append(result_type)
            # TO DO: IF the operands were temporals, free the used space.
            
            
def p_n_quad_mult_div(p):
    'n_quad_mult_div : '
    
    global stack_Operands
    global stack_Types
    global stack_Operators
    global quadruples
    global quad_pointer
            
    if (len(stack_Operators) > 0 and (stack_Operators[-1] == '*' or stack_Operators[-1] == '/')):
            # Take out operands and their types
            right_operand = stack_Operands.pop()
            right_type = stack_Types.pop()
            left_operand = stack_Operands.pop()
            left_type = stack_Types.pop()
            
            operator = stack_Operators.pop()
            
            # Check if types are valid
            result_type = CuboSem.validate_type(operator, left_type, right_type)
            
            if (result_type == -1):
                print("Error: Operation '%s' with mismatched types '%s' and '%s'" % (operator, left_type, right_type))
                p_error(-2)
                
            #If theres no error: Create a temporal and add the quadruple
            result = Addr_Manager.get_Local_Temporal_Dir(result_type)
            directory.Table[scope].add_Temp(result_type)
            
            # Create quadruple
            quadruples.append(Quadruple(operator, left_operand, right_operand, result))
            quad_pointer += 1
            stack_Operands.append(result)
            stack_Types.append(result_type)
            # TO DO: IF the operands were temporals, free the used space.

def p_n_quad_compare(p):
    'n_quad_compare : '
    
    global stack_Operands
    global stack_Types
    global stack_Operators
    global quadruples
    global quad_pointer
            
    if (len(stack_Operators) > 0 and (
        stack_Operators[-1] == '>' or stack_Operators[-1] == '<'
        or stack_Operators[-1] == '>=' or stack_Operators[-1] == '<='
        or stack_Operators[-1] == '==' or stack_Operators[-1] == '!=')):
            # Take out operands and their types
            right_operand = stack_Operands.pop()
            right_type = stack_Types.pop()
            left_operand = stack_Operands.pop()
            left_type = stack_Types.pop()
            
            operator = stack_Operators.pop()
            
            # Check if types are valid
            result_type = CuboSem.validate_type(operator, left_type, right_type)
            
            if (result_type == -1):
                print("Error: Operation '%s' with mismatched types '%s' and '%s'" % (operator, left_type, right_type))
                p_error(-2)
                
            #If theres no error: Create a temporal and add the quadruple
            result = Addr_Manager.get_Local_Temporal_Dir(result_type)
            directory.Table[scope].add_Temp(result_type)
            
            # Create quadruple
            quadruples.append(Quadruple(operator, left_operand, right_operand, result))
            quad_pointer += 1
            stack_Operands.append(result)
            stack_Types.append(result_type)
            # TO DO: IF the operands were temporals, free the used space.

def p_n_quad_and_or(p):
    'n_quad_and_or : '
    
    global stack_Operands
    global stack_Types
    global stack_Operators
    global quadruples
    global quad_pointer
            
    if (len(stack_Operators) > 0 and (stack_Operators[-1] == '&' or stack_Operators[-1] == '|')):
            # Take out operands and their types
            right_operand = stack_Operands.pop()
            right_type = stack_Types.pop()
            left_operand = stack_Operands.pop()
            left_type = stack_Types.pop()
            
            operator = stack_Operators.pop()
            
            # Check if types are valid
            result_type = CuboSem.validate_type(operator, left_type, right_type)
            
            if (result_type == -1):
                print("Error: Operation '%s' with mismatched types '%s' and '%s'" % (operator, left_type, right_type))
                p_error(-2)
                
            #If theres no error: Create a temporal and add the quadruple
            result = Addr_Manager.get_Local_Temporal_Dir(result_type)
            directory.Table[scope].add_Temp(result_type)
            
            # Create quadruple
            quadruples.append(Quadruple(operator, left_operand, right_operand, result))
            quad_pointer += 1
            stack_Operands.append(result)
            stack_Types.append(result_type)
            # TO DO: IF the operands were temporals, free the used space.
    
    
def p_n_false_bottom_start(p):
    'n_false_bottom_start : '
    
    global stack_Operands
    stack_Operators.append('(')
    
def p_n_false_bottom_end(p):
    'n_false_bottom_end : '
    
    if (len(stack_Operators) > 0 and stack_Operators[-1] == '('):
        stack_Operators.pop()
    else:
        print("Error: Parenthesis mismatch")
        p_error(-2)
        
def p_n_quad_if_jump_false(p):
    'n_quad_if_jump_false : '
    
    
    global stack_Operands
    global stack_Types
    global quadruples
    global quad_pointer
    global stack_Jumps
    
    result = stack_Operands.pop()
    tipo_cond = stack_Types.pop()
    
    if (tipo_cond != 'bool'):
        print("Error: Result for condition must be boolean")
        p_error(-2)
        
    quadruples.append(Quadruple('GOTOF', result, '', '')) # Quad to jump to the false section
    quad_pointer += 1
    stack_Jumps.append(quad_pointer - 1)

def p_n_quad_if_else(p):
    'n_quad_if_else : '
    
    global quadruples
    global quad_pointer
    global stack_Jumps
    
    quadruples.append(Quadruple('GOTO', '', '', ''))
    quad_pointer += 1
    
    quad_incomplete = stack_Jumps.pop() # Get the incomplete quad, the one after the evaluation of the expression
    stack_Jumps.append(quad_pointer - 1) # Crumb to right before the false section starts (in case its true, it will jump to the end of the if, skipping this part)
    quadruples[quad_incomplete].set_Result(quad_pointer) # Add where the false section starts
    
def p_n_quad_if_end(p):
    'n_quad_if_end : '
    
    
    global stack_Jumps
    global quadruples
    global quad_pointer
    
    quad_incomplete = stack_Jumps.pop() 
    quadruples[quad_incomplete].set_Result(quad_pointer)
    
def p_n_while_exp(p):
    'n_while_exp : '
    
    global stack_Jumps
    global quad_pointer
    
    stack_Jumps.append(quad_pointer)
    
def p_n_quad_while_false(p):
    'n_quad_while_false : '
    
    global stack_Jumps
    global stack_Operands
    global stack_Types
    global quadruples
    global quad_pointer
    
    result_type = stack_Types.pop()
    if (result_type != 'bool'):
        print("Error: Result for condition must be boolean")
        p_error(-2)
        
    result = stack_Operands.pop()
    quadruples.append(Quadruple('GOTOF', result, '', ''))
    quad_pointer += 1
    
    stack_Jumps.append(quad_pointer - 1)
    
def p_n_quad_while_repeat(p):
    'n_quad_while_repeat : '
    
    global stack_Jumps
    global quadruples
    global quad_pointer
    
    quad_incomplete = stack_Jumps.pop()
    quad_return = stack_Jumps.pop()
    quadruples.append(Quadruple('GOTO', '', '', quad_return))
    quad_pointer += 1
    
    quadruples[quad_incomplete].set_Result(quad_pointer)

def p_n_do_while_start(p):
    'n_do_while_start : '
    
    global stack_Jumps
    global quad_pointer
    
    stack_Jumps.append(quad_pointer)
    
def p_n_quad_do_while_true(p):
    'n_quad_do_while_true : '
    
    global stack_Jumps
    global stack_Operands
    global quad_pointer
    
    start_cycle = stack_Jumps.pop()
    cond = stack_Operands.pop()
    
    quadruples.append(Quadruple('GOTOT', cond, '', start_cycle))
    quad_pointer += 1
    
def p_n_func_start(p):
    'n_func_start : '
    
    global directory
    
    directory.Table[scope].dirStart = quad_pointer
    
def p_n_quad_endfunc(p):
    'n_quad_endfunc : '
    
    global quadruples
    global quad_pointer
    
    quadruples.append(Quadruple('ENDFUNC', '', '', ''))
    quad_pointer += 1
    
        
    #directory.Table[scope].print_VarsTable() 
    
    # Delete varsTable and reset the scope
    del directory.Table[scope].varsTable
    
def p_n_quad_func_era(p):
    'n_quad_func_era : '
    
    global func
    global quadruples
    global quad_pointer
    
    func = p[-1]
    
    if (  not directory.check_Existence(func) ):
        print("Error: Function  '%s' was called but does not exist" % func)
        p_error(-2)
        
    quadruples.append(Quadruple('ERA', func, '', ''))
    quad_pointer += 1
    
    global param_counter
    param_counter = 0
    
def p_n_quad_func_param(p):
    'n_quad_func_param : '
    
    global param_counter
    global quad_pointer
    global stack_Operands
    global stack_Types
    global quadruples
    
    arg = stack_Operands.pop()
    arg_type = stack_Types.pop()
    param_type = directory.get_Param_Type(func, param_counter)
    
    #print(func, param_counter, arg_type, param_type)
    
    if (param_type == 'None'):
        print("Error: Function '%s' was called with more arguments than the declared ones." % func)
        p_error(-2)
    
    if (param_type != arg_type):
        print("Error: Type mismatch in parameter ", param_counter + 1)
        p_error(-2)
    
    quadruples.append(Quadruple('PARAM', arg, 'p#'+str(param_counter), param_type))
    quad_pointer += 1
    param_counter += 1
    
def p_n_func_check_params(p):
    'n_func_check_params : '
    
    global directory
    
    if ( directory.get_Param_Type(func, param_counter) != 'None' ):
        print("Error: Missing arguments for function '%s'" % func)
        p_error(-2)
    
def p_n_quad_func_gosub(p):
    'n_quad_func_gosub : '
    
    global quad_pointer
    global quadruples
    global func
    
    quadruples.append(Quadruple('GOSUB', func, '', ''))
    quad_pointer += 1
    
    func_type = directory.Table[func].get_Type()
    if (func_type != 'void'):
        addr_t = Addr_Manager.get_Local_Temporal_Dir(func_type)
        directory.Table[scope].add_Temp(func_type)
        
        addr = directory.Table['global'].varsTable.Table[func].get_DirV()
        quadruples.append(Quadruple('=', addr, '', addr_t))
        quad_pointer += 1
        
        stack_Operands.append(addr_t)
        stack_Types.append(func_type)
    
def p_n_quad_return(p):
    'n_quad_return : '
    
    return_type = directory.get_Return_Type(scope)
    if (return_type == 'void'):
        print("Error: Function '%s' doesnt have a return type" % scope)
        p_error(-2)
    
    global quad_pointer
    global quadruples
    global stack_Operands
    global stack_Types
    
    result = stack_Operands.pop()
    result_type = stack_Types.pop()
    
    if (result_type != return_type):
        print("Error: Type mismatch in return value")
        p_error(-2)
    
    addr = directory.Table['global'].varsTable.Table[scope].get_DirV()
    quadruples.append(Quadruple('RETURN', result, '', addr))
    quad_pointer += 1
    

# ----------- Methods ----------- #
# From PLY documentation
# Rule to track line numbers
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

# Error rule for syntax errors
def p_error(p):
    if p == -2:
        print("Syntax error in parsing, exiting compilation ...")
        exit()
    if p:
        print("Error de sintaxis antes de '%s'" % p.value, "en la linea", p.lineno)
    else:
        print("Error de sintaxis en EOF")
    parser.error = 1


# Return the parser
parser = yacc.yacc()  


def parse(data, debug=0):
    parser.error = 0
    p = parser.parse(data, debug=debug)
    if parser.error:
        return None
    return p

