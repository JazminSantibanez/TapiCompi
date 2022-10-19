# Path: TapiCompi\compiler\libs\Table_Vars.py

from enums import Type

# Class: Vars_Info
# Description: This class is used to store the information 
#               of the variables
class Vars_Info:
    def __init__(self, type, dirV):
        self.type = type
        self.dirv = dirV
        
    def  get_Type(self):
        return self.type

    def  get_DirV(self):
        return self.dirv


# Class: Vars_Table
# Description: Class that contains the variables table
#   Uses a dictionary where 
#   key: variable name
#   value: Vars_Info object
class Table_Vars:
    
    # Constructor
    # Table_Vars must be initialized with an empty dictionary
    def __init__(self):
        self.Table = {}

    # Adds variable to the table
    def add_Variable(self, name, type, dirV):
        self.Table[name] = Vars_Info(type, dirV)
    
    # Returns variable info from the table
    def get_Variable(self, name):
        return self.Table[name]
    
    # Checks if a variable alreay exists in the table
    # Returns True if it exists, False otherwise
    def check_Existance(self, name):
        return name in self.Table
    
    def print_Table(self):
        print("Table of variables: ")
        
        for key, value in self.Table.items():
            print("Name:", key,
                  "Type: ", value.get_Type(),
                  "DirV: ", value.get_DirV())
        
    
        
# Tests
# if __name__ == '__main__':
#     variables = Table_Vars()
#     variables.add_Variable('a', Type.INT, 100)
#     variables.add_Variable('b', Type.CHAR, 200)
    
#     print(variables.check_Existance('a'))
#     variables.print_Table()
    