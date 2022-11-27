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
        self.scope = self.global_func # Current scope is the global function at the start
        
    # ----------- Helpful prints ------------ #
    
    def print_Quadruples(self):
        print(f' {"Cuadruplos:":^50s}')
        print(f' {"~"*40}')
        lst = [q.to_list() for q in self.quadruples if q != None]
        df = pd.DataFrame(lst, columns=['Operator', 'Left O.', 'Right O.', 'Result'])
        df.index += 1
        pd.set_option('display.max_rows', None)
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
        
        if (isinstance(virtual_addr, int)): # Receives normal virtual address
            # If range is from global variables, use global memory
            if (GLOBAL_INT_START <= virtual_addr <= GLOBAL_BOOL_END):
                return self.global_memory.get_value_local(virtual_addr)
            #if range is from local variables, use current memory
            elif (LOCAL_INT_START <= virtual_addr <= LOCAL_BOOL_END):
                return self.current_memory.get_value_local(virtual_addr)
            # if range is from constants, use constants table
            elif (CONST_INT_START <= virtual_addr <= CONST_BOOL_END):
                return self.const_table[virtual_addr]
            
        if (isinstance(virtual_addr, str)): # Receives virtual address pointer
            pointer = int(virtual_addr[1:-1])
            addr = int(self.get_value(pointer))
            return self.get_value(addr)
    
    def set_value(self, virtual_addr, value):
        
        if (isinstance(virtual_addr, int)): # Receives normal virtual address
            # If range is from global variables, use global memory
            if (GLOBAL_INT_START <= virtual_addr <= GLOBAL_BOOL_END):
                self.global_memory.set_value_local(virtual_addr, value)
            #if range is from local variables, use current memory
            elif (LOCAL_INT_START <= virtual_addr <= LOCAL_BOOL_END):
                self.current_memory.set_value_local(virtual_addr, value)
            # Constants must not be changed.
        
        if (isinstance(virtual_addr, str)): # Receives virtual address pointer
            pointer = int(virtual_addr[1:-1])
            addr = int(self.get_value(pointer))
            return self.set_value(addr, value)
        
    
    def run(self, debug):
        if (debug):
            self.debug()
        
        while (self.instruction_pointer < len(self.quadruples)):
            if (len(self.stack_Contexts) >= 200):
                raise Exception('Error: Calls Stack Overflow.')
                break
            
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
                    if (isinstance(quadruple.result, int) or quadruple.result[0] == '('):
                        print(self.get_value(quadruple.result), end="")                 
                    else:
                        string = quadruple.result[1:-1]
                        if (string == '\\n'):
                            print("\n", end="")
                        else:
                            print(quadruple.result[1:-1], end="")
                    
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
                    if (isinstance(quadruple.left, str)): # b at the start, meaning its a number, not direction
                        left = int(quadruple.left[1:])
                        quadruple.result = int(quadruple.result[1:-1])
                    else:
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
                        raise Exception('Error: Division by zero.')
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
                    # Put the activation record in the context stack 
                    # because is the next in  line to be used.
                    self.stack_Contexts.append(Context(new_memory))
                    
                    self.instruction_pointer += 1
                    
                case 'PARAM': # Set parameter value
                    # quad.left = parameter value
                    # quad.right = parameter position
                    value = self.get_value(quadruple.left)
                    addr = int(quadruple.right[2:])
                    
                    new_memory = self.stack_Contexts[-1].get_Memory()
                    # Use the memory at the top of the stack,. without popping it.
                    
                    match quadruple.result:
                        case 'int':
                            new_memory.local_int[addr] = value
                        case 'float':
                            new_memory.local_float[addr] = value
                        case 'char':
                            new_memory.local_char[addr] = value
                        case 'bool':
                            new_memory.local_bool[addr] = value
                    
                    self.instruction_pointer += 1
                
                case 'GOSUB': # Move IP to the function section
                    # Get the new context
                    new_context = self.stack_Contexts.pop()
                    
                    # "Sleep" the current context and push it to the stack
                    self.stack_Contexts.append(Context(self.current_memory))
                    
                    self.current_memory = new_context.get_Memory()
                    
                    self.stack_Contexts[-1].save_IP(self.instruction_pointer)
                    self.instruction_pointer = self.directory.Table[quadruple.left].get_DirStart()
                    self.scope = self.directory.Table[quadruple.left]
                    
                case 'RETURN': 
                    # Assign return value to the global variable of the same name as the function
                    
                    value = self.get_value(quadruple.left)
                    addr = quadruple.result
                    self.set_value(addr, value)
                    
                    previous_context = self.stack_Contexts.pop()
                    self.current_memory = previous_context.get_Memory()
                    
                    self.instruction_pointer = previous_context.get_IP() + 1 
                    
                case 'ENDFUNC': # Move back to previous context
                    
                    previous_context = self.stack_Contexts.pop()
                    self.current_memory = previous_context.get_Memory()
                    
                    self.instruction_pointer = previous_context.get_IP() + 1
                    
                case 'VERIFY': # Verify array index
                    
                    index = self.get_value(quadruple.left)
                    limSup = quadruple.right
                    
                    if (index < 0 or index >= limSup):
                        raise Exception("Error: Array index out of bounds.")
                    
                    self.instruction_pointer += 1 
                        
                    
                case other:
                    print(f'Error: Operation code {quadruple.operator} not recognized.')
                    self.instruction_pointer += 1