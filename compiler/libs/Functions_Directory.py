from libs.Vars_Table import Vars_Table
from libs.utils.enums import Type
# Path: TapiCompi.compiler.libs


class Function_Info:
    """ 
    Description: This class is used to store the information
                of the functions
    Attributes:
        name (str) : name of the function 
        type (Type) : Type of the function
        varsTable (Vars_Table): table of variables 
    """
    #Constructor
    def __init__(self, name : str, type : Type, dirStart : int):
        '''
        Args:
            name (str) : name of the function
            type (Type) : Type of the function
            dirInicio (int) : virtual direction
        '''
        self.name = name
        self.type = type
        self.varsTable = Vars_Table()
        
        self.dirStart = dirStart
        self.params = []
        
        # Function resources
        self.num_int_local = 0
        self.num_int_temp = 0
        self.num_float_local = 0
        self.num_float_temp = 0
        self.num_char_local = 0
        self.num_char_temp = 0
        self.num_bool_local = 0
        self.num_bool_temp = 0
        
        
    # Getters
    def get_VarsTable(self):
        return self.varsTable
    
    def get_Type(self):
        return self.type

    def get_DirStart(self):
        return self.dirStart
    
    def add_Param(self, type):
        self.params.append(type)
    
    def print_VarsTable(self):
        self.varsTable.print_Table(self.name)
        
    def add_Variable( self, name : str, type, dirV : int):
        match type:
            case 'int':
                self.num_int_local += 1
            case 'float':
                self.num_float_local += 1
            case 'char':
                self.num_char_local += 1
            case 'bool':
                self.num_bool_local += 1
        
        self.varsTable.add_Variable(name, type, dirV)
        
    def add_Local( self, type):
        match type:
            case 'int':
                self.num_int_local += 1
            case 'float':
                self.num_float_local += 1
            case 'char':
                self.num_char_local += 1
            case 'bool':
                self.num_bool_local += 1
                
    def add_Temp( self, type):
        match type:
            case 'int':
                self.num_int_temp += 1
            case 'float':
                self.num_float_temp += 1
            case 'char':
                self.num_char_temp += 1
            case 'bool':
                self.num_bool_temp += 1
        


class Functions_Directory:
    '''
    Description: Class that contains the functions table
    Uses a dictionary where
        * key: variable name
        * value: Function_Info object
        
    Args:
        name (str) : name of the function
        type (Type) : type of the function
        dirInicio (int) : virtual direction
    '''
    # Constructor
    def __init__(self):
        self.Table = {}
    
    
    def add_Function(self, name : str, type : Type, dirV : int):
        '''
        Adds a function to the directory
        
        Args:
            name (str) : name of the function
            type (Type) : type of the function
            dirInicio (int) : virtual direction
        '''
        self.Table[name] = Function_Info(name, type, dirV)
    
    
    def get_Function(self, name):
        return self.Table[name]
    
    
    def check_Existence(self, name):
        return name in self.Table
    
    def add_Func_Param(self, name, type):
        self.Table[name].add_Param(type)
        
    def get_Param_Type(self, name, index):
        if index < len(self.Table[name].params):
            return self.Table[name].params[index]
        return 'None'
    
    def get_Return_Type(self, name):
        return self.Table[name].type
    
    def print_Directory(self):
        print(f'\n {"Directory of functions":^70s}')
        print(f' {"="*80}')
        
        for key, value in self.Table.items():
            if key is not None:
                print(f'> Name: {key:<15s} Type: {value.type:<8s} DirV: {value.dirStart:<8} ParamsType {value.params}')
                print(f'┕ recursos: \n\tint : {value.num_int_local}, {value.num_int_temp} \tfloat: {value.num_float_local}, {value.num_float_temp} \n\tchar: {value.num_char_local}, {value.num_char_temp} \tbool: {value.num_bool_local}, {value.num_bool_temp}')
                """ print(" > Name:", key,
                    "Type:", value.type,
                    "DirV:", value.dirInicio,
                    "params:", value.params) """
            
        #print(" < End of directory")
        
        
""" if __name__ == '__main__':
    directory = Functions_Directory()
    
    directory.add_Function("func1", "int", 100, ["int", "float"])
    directory.add_Function("func2", "float", 200, ["int", "float", "int"])
    
    print("func1 exists: ", directory.check_Existence("func1"))
    print("func3 exists: ", directory.check_Existence("func3"))
    
    directory.Table['func1'] """