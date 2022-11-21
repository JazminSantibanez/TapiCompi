import pandas as pd
from collections import deque

from libs.utils.Constants import *
from vm.Memory import Memory
from vm.Context import Context

class Virtual_Machine:
    def __init__(self, quadruples, directory, const_table):
        self.directory = directory
        self.quadruples = quadruples
        self.instruction_pointer = 1
        # Const_table original = {Value : Addr} optimized for Value search
        # Needs to be changed to optimized for addr search
        # Newe const_table --> {Addr : Value}
        self.const_table = inv_map = {v: k for k, v in const_table.items()}
        
        self.global_func = self.directory.Table['global']
        self.global_memory = Memory(self.global_func.num_int_local,
                                    self.global_func.num_float_local, 
                                    self.global_func.num_char_local, 
                                    self.global_func.num_bool_local,
                                    self.global_func.num_int_temp, 
                                    self.global_func.num_float_temp, 
                                    self.global_func.num_char_temp, 
                                    self.global_func.num_bool_temp)
        self.current_memory = self.global_memory # Memory pointer, points at global memory at the start
        self.stack_Contexts = deque() # Stack that saves the context of the functions. "Sleep" memories
    
    # ----------- Helpful prints ------------ #
    
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
    
    def debug(self):
        self.print_FuncsDirectory()
        print('Constants: ', self.const_table, '\n')
        self.print_Quadruples()

    # ----------- Execution ------------ #
    
    def get_value(self, virtual_addr):
        # If range is from global variables, use global memory
        if (GLOBAL_INT_START <= virtual_addr <= GLOBAL_BOOL_END):
            return self.global_memory.get_value_local(virtual_addr)
        #if range is from local variables, use current memory
        elif (LOCAL_INT_START <= virtual_addr <= LOCAL_BOOL_END):
            return self.current_memory.get_value_local(virtual_addr)
        # if range is from constants, use constants table
        elif (CONST_INT_START <= virtual_addr <= CONST_BOOL_END):
            return self.const_table[virtual_addr]
    
    def set_value(self, virtual_addr, value):
        # If range is from global variables, use global memory
        if (GLOBAL_INT_START <= virtual_addr <= GLOBAL_BOOL_END):
            self.global_memory.set_value_local(virtual_addr, value)
        #if range is from local variables, use current memory
        elif (LOCAL_INT_START <= virtual_addr <= LOCAL_BOOL_END):
            self.current_memory.set_value_local(virtual_addr, value)
        # Constants must not be changed.
        
    
    def run(self, debug):
        if (debug):
            self.debug()
        
        while (self.instruction_pointer < len(self.quadruples)):
            quadruple = self.quadruples[self.instruction_pointer]
            if quadruple == None:
                print('End of quadruples.')
                return
            #print(f'> Op. Code: {quadruple.operator}')
            
            match quadruple.operator:
                case 'GOTO':
                    self.instruction_pointer = quadruple.result
                
                # -- Conditional statements -- #
                
                case 'GOTOF':
                    if (not self.get_value(quadruple.left)):
                        self.instruction_pointer = quadruple.result
                    else:
                        self.instruction_pointer += 1
                    
                case 'GOTOT':
                    if (self.get_value(quadruple.left)):
                        self.instruction_pointer = quadruple.result
                    else:
                        self.instruction_pointer += 1
                
                # -- Sequential statementes -- #
                case 'PRINT':
                    if (isinstance(quadruple.result, int)):
                        print(self.get_value(quadruple.result))
                    else:
                        print(quadruple.result[1:-1])
                    
                    self.instruction_pointer += 1
                    
                case 'READ':
                    value = input()
                    self.set_value(quadruple.result, value)
                    self.instruction_pointer += 1
                    
                case '=':
                    value = self.get_value(quadruple.left)
                    self.set_value(quadruple.result, value) 
                    self.instruction_pointer += 1
                
                # -- Arithmetic operations -- #
                case '+':
                    # If operand is a constant, get value from const table
                    # else, get value from current memory
                    left = self.get_value(quadruple.left)
                    right = self.get_value(quadruple.right)
                    
                    self.set_value(quadruple.result, left + right)
                    self.instruction_pointer += 1
                    
                case '-':
                    left = self.get_value(quadruple.left)
                    right = self.get_value(quadruple.right)
                    
                    self.set_value(quadruple.result, left - right)
                    self.instruction_pointer += 1
                    
                case '*':
                    left = self.get_value(quadruple.left)
                    right = self.get_value(quadruple.right)
                    
                    self.set_value(quadruple.result, left * right)
                    self.instruction_pointer += 1
                
                case '/':
                    left = self.get_value(quadruple.left)
                    right = self.get_value(quadruple.right)
                    
                    if (right == 0):
                        print('Error: Division by zero.')
                        return
                    
                    self.set_value(quadruple.result, left / right)
                    self.instruction_pointer += 1
                
                # -- Relational operations -- #
                case '>':
                    left = self.get_value(quadruple.left)
                    right = self.get_value(quadruple.right)
                    
                    self.set_value(quadruple.result, left > right)
                    self.instruction_pointer += 1
                    
                case '<':
                    left = self.get_value(quadruple.left)
                    right = self.get_value(quadruple.right)
                    
                    self.set_value(quadruple.result, left < right)
                    self.instruction_pointer += 1
                    
                case '>=':
                    left = self.get_value(quadruple.left)
                    right = self.get_value(quadruple.right)
                    
                    self.set_value(quadruple.result, left >= right)
                    self.instruction_pointer += 1
                    
                case '<=':
                    left = self.get_value(quadruple.left)
                    right = self.get_value(quadruple.right)
                    
                    self.set_value(quadruple.result, left <= right)
                    self.instruction_pointer += 1
                
                case '==':
                    left = self.get_value(quadruple.left)
                    right = self.get_value(quadruple.right)
                    
                    self.set_value(quadruple.result, left == right)
                    self.instruction_pointer += 1
                
                case '!=':
                    left = self.get_value(quadruple.left)
                    right = self.get_value(quadruple.right)
                    
                    self.set_value(quadruple.result, left != right)
                    self.instruction_pointer += 1
                    
                # -- Logical operations -- #
                    
                case '&':
                    left = self.get_value(quadruple.left)
                    right = self.get_value(quadruple.right)
                    
                    self.set_value(quadruple.result, left and right)
                    self.instruction_pointer += 1
                    
                case '|':
                    left = self.get_value(quadruple.left)
                    right = self.get_value(quadruple.right)
                    
                    self.set_value(quadruple.result, left or right)
                    self.instruction_pointer += 1
                
                # -- Functions -- #
                
                case 'ERA': # Create new memory for function
                    # quad.left = function name
                    
                    self.stack_Contexts.append(Context(self.current_memory)) # Save current memory
                    func = self.directory.get_Function(quadruple.left)
                    # Create activation record
                    new_memory = Memory(
                                        func.num_int_local,
                                        func.num_float_local, 
                                        func.num_char_local, 
                                        func.num_bool_local,
                                        func.num_int_temp, 
                                        func.num_float_temp, 
                                        func.num_char_temp, 
                                        func.num_bool_temp)                    
                    self.current_memory = new_memory
                    
                    self.instruction_pointer += 1
                    
                case 'PARAM': # Set parameter value
                    # quad.left = parameter value
                    # quad.right = parameter position
                    value = self.get_value(quadruple.left)
                    addr = int(quadruple.right[2:])
                    
                    match quadruple.result:
                        case 'int':
                            self.current_memory.local_int[addr] = value
                        case 'float':
                            self.current_memory.local_float[addr] = value
                        case 'char':
                            self.current_memory.local_char[addr] = value
                        case 'bool':
                            self.current_memory.local_bool[addr] = value
                    
                    self.instruction_pointer += 1
                
                case 'GOSUB': # Move IP to the function section
                    self.stack_Contexts[-1].save_IP(self.instruction_pointer)
                    self.instruction_pointer = self.directory.Table[quadruple.left].get_DirStart()
                    
                case 'ENDFUNC': # Return to previous context
                    self.current_memory = None
                    previous_context = self.stack_Contexts.pop()
                    self.current_memory = previous_context.get_Memory()
                    self.instruction_pointer = previous_context.get_IP() + 1
                    
                case other:
                    print(f'Error: Operation code {quadruple.operator} not recognized.')
                    self.instruction_pointer += 1