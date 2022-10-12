from ply import *
import TapiCompi_lex
import libs.CuboSem

tokens = TapiCompi_lex.tokens

#  Definition of rules

## -- <programa> --
def p_programa(p):
    'programa : aux_prog aux_prog2 MAIN lPAREN rPAREN cuerpo '
    p[0] = "Success"

def p_aux_prog(p):
    '''aux_prog : dec_var
                | empty'''

def p_aux_prog2(p):
    '''aux_prog2 : dec_func aux_prog2
                 | empty'''


## -- <cuerpo> --
def p_cuerpo(p):
    'cuerpo : aux_cuerpo bloque'

def p_aux_cuerpo(p):
    '''aux_cuerpo : dec_var
                  | empty'''


## -- <dec_var> --
def p_dec_var(p):
    ' dec_var : VAR aux_dv'

def p_aux_dv(p):
    'aux_dv : aux_dv2 aux_dv3'

def p_aux_dv2(p):
    '''aux_dv2 : tipo_s 
                | tipo_c'''

def p_aux_dv3(p):
    'aux_dv3 : ID aux_dv4 aux_dv6 SEP_SEMICOLON aux_dv7'

def p_aux_dv4(p):
    '''aux_dv4 : arr aux_dv5
               | empty'''

def p_aux_dv5(p):
    '''aux_dv5 : arr
               | empty'''

def p_aux_dv6(p):
    '''aux_dv6 : SEP_COMMA aux_dv3
               | empty'''

def p_aux_dv7(p):
    '''aux_dv7 : aux_dv
               | empty'''


# -- <arr> --
def p_arr(p):
    'arr : lBRACKET aux_arr rBRACKET'

def p_aux_arr(p):
    '''aux_arr : ID
               | CTE_I'''


# -- <call_var> --
def p_call_var(p):
    'call_var : ID aux_cv'

def p_aux_cv(p):
    '''aux_cv : arr aux_cv2
              | empty'''

def p_aux_cv2(p):
    '''aux_cv2 : arr
               | empty'''


# -- <tipo_s> --
def p_tipo_s(p):
    '''tipo_s : INT
              | FLOAT
              | CHAR'''


# -- <tipo_c> --
def p_tipo_c(p):
    '''tipo_c : DATAFRAME
              | FILE '''


## -- <params> --
def p_params(p):
    'params : tipo_s call_var aux_params'

def p_aux_params(p):
    '''aux_params : SEP_COMMA params
                  | empty'''


# -- <dec_func> --
def p_dec_func(p):
    '''dec_func : func_void 
                | func_return'''


# -- <func_void> --
def p_func_void(p):
    'func_void : FUNC VOID ID lPAREN aux_fv rPAREN cuerpo'


def p_aux_fv(p):
    '''aux_fv : params
              | empty'''


# -- <func_return> --
def p_func_return(p):
    'func_return : FUNC tipo_s ID lPAREN aux_fr rPAREN lBRACE aux_fr2 bloque_return rBRACE'

def p_aux_fr(p):
    '''aux_fr : params
              | empty'''

def p_aux_fr2(p):
    '''aux_fr2 : dec_var
               | empty'''

## -- <return> --
def p_return(p):
    'return : RETURN lPAREN h_exp rPAREN SEP_SEMICOLON'


## -- <call_func>
def p_call_func(p):
    'call_func : ID lPAREN aux_cf rPAREN'

def p_aux_cf(p):
    '''aux_cf : h_exp aux_cf2
              | empty'''
              
def p_aux_cf2(p):
    '''aux_cf2 : SEP_COMMA aux_cf
               | empty'''
             
  
## -- <bloque> --
def p_bloque(p):
    'bloque : lBRACE estatuto SEP_SEMICOLON aux_bloque aux_bloque2 rBRACE'
    
def p_aux_bloque(p):
    '''aux_bloque : COMENTARIO
                  | empty'''
    
def p_aux_bloque2(p):
    '''aux_bloque2 : estatuto SEP_SEMICOLON aux_bloque aux_bloque2
                  | empty'''


## -- <bloque_return>
def p_bloque_return(p):
    'bloque_return : estatuto SEP_SEMICOLON aux_bloque aux_bloque2 return'
        
                  
## -- <estatuto> --
def p_estatuto(p):
    '''estatuto : asignacion
                | call_func
                | leer
                | escribir
                | condicion
                | ciclo_while
                | ciclo_for
                | COMENTARIO'''


## -- <asignacion> --
def p_asignacion(p):
    'asignacion : call_var OP_ASSIGN h_exp' 

  
## -- <leer> --
def p_leer(p):
    'leer : READ lPAREN call_var aux_leer rPAREN'

def p_aux_leer(p):
    '''aux_leer : SEP_COMMA call_var aux_leer
                | empty'''
                
                
## -- <escribir> --
def p_escribir(p):
    'escribir : PRINT lPAREN aux_escribir aux_escribir2 rPAREN'

def p_aux_escribir(p):
    '''aux_escribir : h_exp
                    | LETRERO
                    | CTE_CHAR'''
def p_aux_escribir2(p):
    '''aux_escribir2 : SEP_COMMA aux_escribir aux_escribir2
                     | empty'''
        
                    
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
    'h_exp : s_exp aux_hexp'

def p_aux_hexp(p):
    '''aux_hexp : OP_AND h_exp
                | OP_OR h_exp
                | empty'''


## -- <s_exp> --
def p_s_exp(p):
    's_exp : exp aux_sexp'
    
def p_s_aux_sexp(p):
    '''aux_sexp : aux_sexp2 exp
                | empty'''

def p_aux_sexp2(p):
    '''aux_sexp2 : OP_EQ s_exp
                | OP_NEQ s_exp
                | OP_GT s_exp
                | OP_LT s_exp
                | OP_GTE s_exp
                | OP_LTE s_exp
                | empty'''


## -- <exp> --
def p_exp(p):
    'exp : termino aux_exp'

def p_aux_exp(p):
    '''aux_exp : OP_ADD exp
               | OP_SUBTR exp
               | empty'''
    if p[1] == '+':
        p[0] == p[1] + p[2]
    elif p[1] == '-':
        p[0] == p[1] - p[2]
           
               
## -- <termino> --
def p_termino(p):
    'termino : factor aux_termino'

def p_aux_termino(p):
    '''aux_termino : OP_MULT termino
                   | OP_DIV termino
                   | empty'''
    if p[1] == '*':
        p[0] == p[1] * p[2]
    elif p[1] == '/':
        p[0] == p[1] / p[2]
           
                   
## -- <factor> --
def p_factor(p):
    'factor : aux_factor aux_factor2'
    
def p_aux_factor(p):
    '''aux_factor : OP_ADD 
                    | OP_SUBTR 
                    | empty'''
    if p[1] == '+':
        p[0] == p[1]
    elif p[1] == '-':
        p[0] == -p[1]
                    
def p_aux_factor2(p):
    '''aux_factor2 : CTE_I
                   | CTE_F
                   | h_exp
                   | call_func
                   | call_var'''

# Error rule for syntax errors
def p_error(p):
    if p:
        print("Error de sintaxis en '%s'" % p.value)
    else:
        print("Error de sintaxis en EOF")
    parser.error = 1


def p_empty(p):
    'empty :'
    pass

# Build the parser
parser = yacc.yacc()  


def parse(data, debug=0):
    parser.error = 0
    p = parser.parse(data, debug=debug)
    if parser.error:
        return None
    return p

