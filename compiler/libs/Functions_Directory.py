from Vars_Table import Vars_Table
from enums import Type
# Path: TapiCompi.compiler.libs


class Function_Info:
    """ 
    Description: This class is used to store the information
                of the functions
    Attributes: 
        type (Type) : Type of the function
        dirV (int) : virtual direction
        numParams (int) : # of parameters
        parms (list) : type of parameters
        varsTable (Vars_Table): table of variables 
    """
    #Constructor
    def __init__(self, type : Type, dirV : int, params : list):
        '''
        Args:
            type (Type) : Type of the function
            dirV (int) : virtual direction
            params (list) : type of parameters
        '''
        self.type = type
        self.dirV = dirV
        self.params = params
        self.numParams = len(params)
        self.varsTable = Vars_Table()
        
    # Getters
    def get_Type(self):
        return self.type
    
    def get_DirV(self):
        return self.dirV

    def get_Params(self):
        return self.params
    
    def get_NumParams(self):
        return self.numParams
        


class Functions_Directory:
    '''
    Description: Class that contains the functions table
    Uses a dictionary where
        * key: variable name
        * value: Function_Info object
        
    Args:
        name (str) : name of the function
        type (Type) : type of the function
        dirV (int) : virtual direction
    '''
    # Constructor
    def __init__(self):
        self.Table = {}
    
    
    def add_Function(self, name : str, type : Type, dirV : int, params : list):
        '''
        Adds a function to the directory
        
        Args:
            name (str) : name of the function
            type (Type) : type of the function
            dirV (int) : virtual direction
            params (list) : type of parameters
        '''
        self.Table[name] = Function_Info(type, dirV, params)
    
    
    def get_Function(self, name):
        return self.Table[name]
    
    
    def check_Existence(self, name):
        return name in self.Table
    
    
    def print_Directory(self):
        print("\n> Directory of functions: ")
        
        for key, value in self.Table.items():
            print("  Name:", key,
                  "Type: ", value.get_Type(),
                  "DirV: ", value.get_DirV(),
                  "# Params: ", value.get_NumParams(),
                  "ParamsType: ", value.get_Params())
            
        print("< End of directory")
        
        
""" if __name__ == '__main__':
    directory = Functions_Directory()
    
    directory.add_Function("func1", "int", 100, ["int", "float"])
    directory.add_Function("func2", "float", 200, ["int", "float", "int"])
    
    print("func1 exists: ", directory.check_Existence("func1"))
    print("func3 exists: ", directory.check_Existence("func3"))
    
    directory.print_Directory() """