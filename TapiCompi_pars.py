from ply import *
import TapiCompi_lex

tokens = TapiCompi_lex.tokens

# Definition of rules
def p_programa(p):
    '''
    programa : bloque
    '''
    p[0] = "Success"



# Error rule for syntax errors
def p_error(p):
        print("Error: {} ".format(p))
        
def p_empty(p):
    'empty :'
    pass

parser = yacc.yacc()

def parse(data, debug=0):
    parser.error = 0
    p = parser.parse(data, debug=debug)
    if parser.error:
        return None
    return p