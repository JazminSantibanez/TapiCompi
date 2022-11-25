import sys
from src.TapiCompi_pars import parser, quadruples, directory, const_table
from src.TapiCompi_lex import Tokenize
from vm.Virtual_Machine import Virtual_Machine

def run(code):
    #Tokenize(code)
    try:
        #Tokenize(data)
        if(parser.parse(data) == "Success"):
            #print('\nCompilacion exitosa')
            vm = Virtual_Machine(quadruples, directory, const_table)
            if (debug == 1):
                vm.run(True)
            else:
                vm.run(False)
                        
        else:
            print('\nCompilacion fallida')
            return
        
    except EOFError:
        print(EOFError)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if (len(sys.argv) > 2):
            global debug
            debug = sys.argv[2]
            
        data = open(sys.argv[1]).read()
        run(data)
    else:
        print("Error: No se ha ingresado un archivo de entrada.")
    
