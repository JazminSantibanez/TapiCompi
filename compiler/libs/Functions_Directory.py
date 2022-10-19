from Vars_Table import Vars_Table

# Path: TapiCompi.compiler.libs

# Class: Function_Info
# Description: This class is used to store the information
#               of the functions
# Attributes: Type, dirV (virtual direction), 
#               numParams (# of parameters), parms (type of parameters)
class Function_Info:
    #Constructor
    def __init__(self, type, dirV, params):
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
        

# Class: Table_Functions
# Description: 
class Functions_Directory:
    # Constructor
    def __init__(self):
        self.Table = {}
        
    def add_Function(self, name, type, dirV, params):
        self.Table[name] = Function_Info(type, dirV, params)
    
    def get_Function(self, name):
        return self.Table[name]
    
    def check_Existence(self, name):
        return name in self.Table
    
    def print_Directory(self):
        print("\n> Directory of functions: ")
        
        for key, value in self.Table.items():
            print("Name:", key,
                  "Type: ", value.get_Type(),
                  "DirV: ", value.get_DirV(),
                  "# Params: ", value.get_NumParams(),
                  "ParamsType: ", value.get_Params())
            
        print("> End of directory")
        
        
""" if __name__ == '__main__':
    directory = Functions_Directory()
    
    directory.add_Function("func1", "int", 100, ["int", "float"])
    directory.add_Function("func2", "float", 200, ["int", "float", "int"])
    
    print("func1 exists: ", directory.check_Existence("func1"))
    print("func3 exists: ", directory.check_Existence("func3"))
    
    directory.print_Directory() """