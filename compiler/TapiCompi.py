import sys
from src.TapiCompi_pars import parser, quadruples, directory, const_table
from src.TapiCompi_lex import Tokenize
from vm.Virtual_Machine import Virtual_Machine

def run(code, flags):
    #Tokenize(code)
    try:
        #Tokenize(data)
        if(parser.parse(data) == "Success"):
            #print('\nCompilacion exitosa')
            vm = Virtual_Machine(quadruples, directory, const_table)
            if (flags == '--d'):
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
        flags = None
        if (len(sys.argv) > 2):
            flags = sys.argv[2]
            
        data = open(sys.argv[1]).read()
        run(data, flags)
    else:
        print("Error: No se ha ingresado un archivo de entrada.")
    
