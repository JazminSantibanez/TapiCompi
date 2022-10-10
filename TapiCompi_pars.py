from ply import *
import TapiCompi_lex

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
    'aux_dv : aux_dv2 au_dv3'

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

# Error rule for syntax errors
def p_error(p):
        print("Error: {} ".format(p))
        
def p_empty(p):
    'empty :'
    pass

parser = yacc.yacc() # Build the parser

def parse(data, debug=0):
    parser.error = 0
    p = parser.parse(data, debug=debug)
    if parser.error:
        return None
    return p
