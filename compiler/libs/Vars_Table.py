""" 
 Vars_Table module is a table of variables for TapiCompi language.
 It stores the variables declared in the program.
 Uses a dictionary to save the variables.
   - key : variable name
   - value : Object Vars_Info 
"""


# Path: TapiCompi.compiler.libs

from libs.enums import Type


class Var_Info:
    """ 
    Description: This class is used to store the information 
            of the variables
    Attributes:
        type (Type) : Type of the variable
        dirV (int) : Virtual direction 
    """
    def __init__(self, type : Type, dirV : int):
        '''
        Args:
            type (Type) : Type of the variable
            dirV (int) : Virtual direction
        '''
        self.type = type 
        self.dirV = dirV
        self.numDimensions = 0
        self.sizeDimensions = []
        
    def  get_Type(self):
        return self.type

    def  get_DirV(self):
        return self.dirV
    

    def get_NumDimensions(self):
        return self.numDimensions
    
    def get_SizeDimensions(self):
        return self.sizeDimensions
    
    def add_Dimension(self, size):
        self.numDimensions += 1
        self.sizeDimensions.append(size)


class Vars_Table:
    """ 
    Description: Class that contains the variables table \n
    Uses a dictionary where 
        * key: variable name
        * value: Var_Info object
    """
        
    # Constructor
    # Vars_Table must be initialized with an empty dictionary
    def __init__(self):
        self.Table = {}

    # Adds variable to the table
    def add_Variable(self, name : str, type : Type, dirV : int):
        '''
        Args:
            type (Type) : type of the variable
            dirV (int) : virtual direction
        '''
        self.Table[name] = Var_Info(type, dirV)
    
    # Returns variable info from the table
    def get_Variable(self, name):
        return self.Table[name]
    
    # Checks if a variable alreay exists in the table
    # Returns True if it exists, False otherwise
    def check_Existence(self, name):
        return name in self.Table
    
    def add_Var_Dimension(self, name, size):
        self.Table[name].add_Dimension(size)
    
    def print_Table(self, nameFunc):
        print("\n-- Table of variables for", {nameFunc}, ": --")
        
        for key, value in self.Table.items():
            print(" > Name:", key,
                  "Type: ", value.get_Type(),
                  "DirV: ", value.get_DirV(),
                  "NumDimensions: ", value.get_NumDimensions(),
                  "SizeDimensions: ", value.get_SizeDimensions())
        
        #print(" < End of table")    
    
# Tests
""" if __name__ == '__main__':
    variables = Vars_Table()
    variables.add_Variable('a', Type.INT, 100)
    variables.add_Variable('b', Type.CHAR, 200)
    
    print(variables.check_Existence('a'))
    variables.print_Table() """
    