import pandas as pd
from libs.utils.Constants import *
from vm.Memory import Memory

class Virtual_Machine:
    def __init__(self, quadruples, directory, const_table):
        self.directory = directory
        self.quadruples = quadruples
        self.instruction_pointer = 1
        # Const_table original = {Value : Addr} optimized for Value search
        # Needs to be changed to optimized for addr search
        # Newe const_table --> {Addr : Value}
        self.const_table = inv_map = {v: k for k, v in const_table.items()}
                    
    def print_Quadruples(self):
        print(f' {"Cuadruplos:":^50s}')
        print(f' {"~"*40}')
        lst = [q.to_list() for q in self.quadruples if q != None]
        df = pd.DataFrame(lst, columns=['Operator', 'Left O.', 'Right O.', 'Result'])
        df.index += 1
        print(df)
        print(f' {"~"*40}')
        
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
            #print(f'> Op. Code: {quadruple.operator}')
            match quadruple.operator:
                case 'GOTO':
                    self.instruction_pointer = quadruple.result
                
                case 'PRINT':
                    if (isinstance(quadruple.result, int)):
                        print(memory.get_value(quadruple.result))
                    else:
                        print(quadruple.result[1:-1])
                    
                    self.instruction_pointer += 1
                    
                case 'READ':
                    value = input()
                    memory.set_value(quadruple.result, value)
                    self.instruction_pointer += 1
                    
                case '=':
                    addr = quadruple.left
                    if ( addr >= CONST_INT_START and addr <= CONST_BOOL_END):
                       value = self.const_table[addr]
                    else:
                        value = memory.get_value(quadruple.left)
                    memory.set_value(quadruple.result, value)
                    self.instruction_pointer += 1
                
                case '+':
                    if (quadruple.left >= CONST_INT_START and quadruple.left <= CONST_FLOAT_END):
                        left = self.const_table[quadruple.left]
                    else:
                        left = memory.get_value(quadruple.left)
                        
                    if (quadruple.right >= CONST_INT_START and quadruple.right <= CONST_FLOAT_END):
                        right = self.const_table[quadruple.right]
                        
                    else:
                        right = memory.get_value(quadruple.right)
                    res = left + right
                    memory.set_value(quadruple.result, res)
                    self.instruction_pointer += 1
                
                case other:
                    print(f'Error: Operation code {quadruple.operator} not recognized.')
                    self.instruction_pointer += 1