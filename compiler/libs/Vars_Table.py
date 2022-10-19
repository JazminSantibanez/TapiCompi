""" 
 Vars_Table module is a table of variables for TapiCompi language.
 It stores the variables declared in the program.
 Uses a dictionary to save the variables.
   - key : variable name
   - value : Object Vars_Info 
"""


# Path: TapiCompi.compiler.libs

from enums import Type

# Class: Vars_Info
# Description: This class is used to store the information 
#               of the variables
# Attributes: Type, dirV (virtual direction)
class Var_Info:
    def __init__(self, type, dirV):
        self.type = type
        self.dirV = dirV
        
    def  get_Type(self):
        return self.type

    def  get_DirV(self):
        return self.dirV


# Class: Vars_Table
# Description: Class that contains the variables table
#   Uses a dictionary where 
#   key: variable name
#   value: Vars_Info object
class Vars_Table:
    
    # Constructor
    # Vars_Table must be initialized with an empty dictionary
    def __init__(self):
        self.Table = {}

    # Adds variable to the table
    def add_Variable(self, name, type, dirV):
        self.Table[name] = Var_Info(type, dirV)
    
    # Returns variable info from the table
    def get_Variable(self, name):
        return self.Table[name]
    
    # Checks if a variable alreay exists in the table
    # Returns True if it exists, False otherwise
    def check_Existence(self, name):
        return name in self.Table
    
    def print_Table(self):
        print("> Table of variables: ")
        
        for key, value in self.Table.items():
            print("Name:", key,
                  "Type: ", value.get_Type(),
                  "DirV: ", value.get_DirV())
        
        print("> End of table")    
    
# Tests
""" if __name__ == '__main__':
    variables = Vars_Table()
    variables.add_Variable('a', Type.INT, 100)
    variables.add_Variable('b', Type.CHAR, 200)
    
    print(variables.check_Existence('a'))
    variables.print_Table() """
    