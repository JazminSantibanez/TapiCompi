from src.TapiCompi_pars import parser
from src.TapiCompi_lex import Tokenize
import sys


def run(code):
    try:
        #Tokenize(data)
        if(parser.parse(data) == "Success"):
            print('\nCompilacion exitosa')
        else:
            print('\nCompilacion fallida')
        
    except EOFError:
        print(EOFError)
    

if __name__ == '__main__':
    if len(sys.argv) > 1:
        data = open(sys.argv[1]).read()
        run(data)
    else:
        print("Error: No se ha ingresado un archivo de entrada.")
    
