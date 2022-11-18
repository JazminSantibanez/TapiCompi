import pandas as pd
from vm.Memory import Memory

class Virtual_Machine:
    def __init__(self, quadruples, directory):
        self.directory = directory
        self.quadruples = quadruples
        self.instruction_pointer = 1
                    
    def print_Quadruples(self):
        print(f' {"Cuadruplos:":^50s}')
        print(f' {"*"*50}')
        lst = [q.to_list() for q in self.quadruples if q != None]
        df = pd.DataFrame(lst, columns=['Operator', 'Left O.', 'Right O.', 'Result'])
        df.index += 1
        print(df)
        
    def print_FuncsDirectory(self):
        self.directory.print_Directory()
        print('\n')
        
    def run(self):
        f_global = self.directory.Table['global']
        memory = Memory(f_global.num_int_local, f_global.num_float_local, f_global.num_char_local, f_global.num_bool_local,
                    f_global.num_int_temp, f_global.num_float_temp, f_global.num_char_temp, f_global.num_bool_temp)
        
        while (self.instruction_pointer < len(self.quadruples)):
            quadruple = self.quadruples[self.instruction_pointer]
            if quadruple == None:
                print('End of quadruples.')
                return
            print(f'> Op. Code: {quadruple.operator}')
            match quadruple.operator:
                case 'GOTO':
                    self.instruction_pointer = quadruple.result
                case other:
                    #print(f'Error: Operation code {quadruple.operator} not recognized.')
                    self.instruction_pointer += 1