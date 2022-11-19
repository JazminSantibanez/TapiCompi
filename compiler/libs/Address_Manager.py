from libs.utils.Constants import *

# Class to map the variables to a virtual direction

# Each pointer points to the next available virtual direction
class Address_Manager:
    def __init__(self): 
        # Global variables
        self.global_int_pointer = GLOBAL_INT_START
        self.global_float_pointer = GLOBAL_FLOAT_START
        self.global_char_pointer = GLOBAL_CHAR_START
        self.global_bool_pointer = GLOBAL_BOOL_START
        
        # Local & temporal variables
        self.local_int_pointer = LOCAL_INT_START
        self.local_int_temp_pointer = LOCAL_INT_TEMP_START
        
        self.local_float_pointer = LOCAL_FLOAT_START
        self.local_float_temp_pointer = LOCAL_FLOAT_TEMP_START
        
        self.local_char_pointer = LOCAL_CHAR_START
        self.local_char_temp_pointer = LOCAL_CHAR_TEMP_START
        
        self.local_bool_pointer = LOCAL_BOOL_START
        self.local_bool_temp_pointer = LOCAL_BOOL_TEMP_START
        
        # Constant variables
        self.const_int_pointer = CONST_INT_START
        self.const_float_pointer = CONST_FLOAT_START
        self.const_char_pointer = CONST_CHAR_START
        self.const_bool_pointer = CONST_BOOL_START
    
    #Getters for new directions
    def get_Global_Int_Dir(self):
        if (self.global_int_pointer > GLOBAL_INT_END):
            print("Error: Global Int pointer out of range")
            return -1
        else:
            self.global_int_pointer += 1
            return self.global_int_pointer - 1
        
    def get_Global_Float_Dir(self):
        if (self.global_float_pointer > GLOBAL_FLOAT_END):
            print("Error: Global Float pointer out of range.")
            return -1
        else:
            self.global_float_pointer += 1
            return self.global_float_pointer - 1
    
    def get_Global_Char_Dir(self):
        if (self.global_char_pointer > GLOBAL_CHAR_END):
            print("Error: Global Char pointer out of range.")
            return -1
        else:
            self.global_char_pointer += 1
            return self.global_char_pointer - 1
        
    def get_Global_Bool_Dir(self):
        if (self.global_bool_pointer > GLOBAL_BOOL_END):
            print("Error: Global Bool pointer out of range.")
            return -1
        else:
            self.global_bool_pointer += 1
            return self.global_bool_pointer - 1
        
    def get_Local_Int_Dir(self):
        if (self.local_int_pointer >= LOCAL_INT_TEMP_START):
            print("Error: Local Int pointer out of range.")
            return -1
        else:
            self.local_int_pointer += 1
            return self.local_int_pointer - 1
        
    def get_Local_Int_Temp_Dir(self):
        if (self.local_int_temp_pointer > LOCAL_INT_END):
            print("Error: Local Int Temp pointer out of range.")
            return -1
        else:
            self.local_int_temp_pointer += 1
            return self.local_int_temp_pointer - 1
    
    def get_Local_Float_Dir(self):
        if (self.local_float_pointer >= LOCAL_FLOAT_TEMP_START):
            print("Error: Local Float pointer out of range.")
            return -1
        else:
            self.local_float_pointer += 1
            return self.local_float_pointer - 1
        
    def get_Local_Float_Temp_Dir(self):
        if (self.local_float_temp_pointer > LOCAL_FLOAT_END):
            print("Error: Local Float Temp pointer out of range.")
            return -1
        else:
            self.local_float_temp_pointer += 1
            return self.local_float_temp_pointer - 1
        
    def get_Local_Char_Dir(self):
        if (self.local_char_pointer >= LOCAL_CHAR_TEMP_START):
            print("Error: Local Char pointer out of range.")
            return -1
        else:
            self.local_char_pointer += 1
            return self.local_char_pointer - 1
        
    def get_Local_Char_Temp_Dir(self):
        if (self.local_char_temp_pointer > LOCAL_CHAR_END):
            print("Error: Local Char Temp pointer out of range.")
            return -1
        else:
            self.local_char_temp_pointer += 1
            return self.local_char_temp_pointer - 1
        
        
    def get_Local_Bool_Dir(self):
        if (self.local_bool_pointer > LOCAL_BOOL_TEMP_START):
            print("Error: Local Bool pointer out of range.")
            return -1
        else:
            self.local_bool_pointer += 1
            return self.local_bool_pointer - 1
        
    def get_Local_Bool_Temp_Dir(self):
        if (self.local_bool_temp_pointer > LOCAL_BOOL_END):
            print("Error: Local Bool Temp pointer out of range.")
            return -1
        else:
            self.local_bool_temp_pointer += 1
            return self.local_bool_temp_pointer - 1
        
    def get_Const_Int_Dir(self):
        if (self.const_int_pointer > CONST_INT_END):
            print("Error: Const Int pointer out of range.")
            return -1
        else: 
            self.const_int_pointer += 1
            return self.const_int_pointer - 1
    
    def get_Const_Float_Dir(self):
        if (self.const_float_pointer > CONST_FLOAT_END):
            print("Error: Const Float pointer out of range.")
            return -1
        else:
            self.const_float_pointer += 1
            return self.const_float_pointer - 1
        
    def get_Const_Char_Dir(self):
        if (self.const_char_pointer > CONST_CHAR_END):
            print("Error: Const Char pointer out of range.")
            return -1
        else:
            self.const_char_pointer += 1
            return self.const_char_pointer - 1
        
    def get_Const_Bool_Dir(self):
        if (self.const_bool_pointer > CONST_BOOL_END):
            print("Error: Const Bool pointer out of range.")
            return -1
        else:
            self.const_bool_pointer += 1
            return self.const_bool_pointer - 1
        
    def get_Global_Dir(self,  type):
        match type:
            case "int":
                return self.get_Global_Int_Dir()
            case "float":
                return self.get_Global_Float_Dir()
            case "char":
                return self.get_Global_Char_Dir()
            case "bool":
                return self.get_Global_Bool_Dir()
            
    def get_Local_Dir(self,  type):
        match type:
            case "int":
                return self.get_Local_Int_Dir()
            case "float":
                return self.get_Local_Float_Dir()
            case "char":
                return self.get_Local_Char_Dir()
            case "bool":
                return self.get_Local_Bool_Dir()
        
    
    def get_Local_Temporal_Dir(self, type):
        match type:
            case "int":
                return self.get_Local_Int_Temp_Dir()
            case "float":
                return self.get_Local_Float_Temp_Dir()
            case "char":
                return self.get_Local_Char_Temp_Dir()
            case "bool":
                return self.get_Local_Bool_Temp_Dir()
        
    def reset_local(self):
        # Local & temporal variables
        self.local_int_pointer = LOCAL_INT_START
        self.local_int_temp_pointer = LOCAL_INT_TEMP_START
        
        self.local_float_pointer = LOCAL_FLOAT_START
        self.local_float_temp_pointer = LOCAL_FLOAT_TEMP_START
        
        self.local_char_pointer = LOCAL_CHAR_START
        self.local_char_temp_pointer = LOCAL_CHAR_TEMP_START
        
        self.local_bool_pointer = LOCAL_BOOL_START
        self.local_bool_temp_pointer = LOCAL_BOOL_TEMP_START
        
# Conversion of virtual address to memory array index
def get_Memory_Index(virtual_addr):
    if (virtual_addr >= GLOBAL_INT_START and virtual_addr <= GLOBAL_INT_END):
        return virtual_addr - GLOBAL_INT_START
    elif (virtual_addr >= GLOBAL_FLOAT_START and virtual_addr <= GLOBAL_FLOAT_END):
        return virtual_addr - GLOBAL_FLOAT_START
    elif (virtual_addr >= GLOBAL_CHAR_START and virtual_addr <= GLOBAL_CHAR_END):
        return virtual_addr - GLOBAL_CHAR_START
    elif (virtual_addr >= GLOBAL_BOOL_START and virtual_addr <= GLOBAL_BOOL_END):
        return virtual_addr - GLOBAL_BOOL_START
    elif (virtual_addr >= LOCAL_INT_START and virtual_addr < LOCAL_INT_TEMP_START):
        return virtual_addr - LOCAL_INT_START
    elif (virtual_addr >= LOCAL_INT_TEMP_START and virtual_addr <= LOCAL_INT_END):
        return virtual_addr - LOCAL_INT_TEMP_START
    elif (virtual_addr >= LOCAL_FLOAT_START and virtual_addr < LOCAL_FLOAT_TEMP_START):
        return virtual_addr - LOCAL_FLOAT_START
    elif (virtual_addr >= LOCAL_FLOAT_TEMP_START and virtual_addr <= LOCAL_FLOAT_END):
        return virtual_addr - LOCAL_FLOAT_TEMP_START
    elif (virtual_addr >= LOCAL_CHAR_START and virtual_addr < LOCAL_CHAR_TEMP_START):
        return virtual_addr - LOCAL_CHAR_START
    elif (virtual_addr >= LOCAL_CHAR_TEMP_START and virtual_addr <= LOCAL_CHAR_END):
        return virtual_addr - LOCAL_CHAR_TEMP_START
    elif (virtual_addr >= LOCAL_BOOL_START and virtual_addr < LOCAL_BOOL_TEMP_START):
        return virtual_addr - LOCAL_BOOL_START
    elif (virtual_addr >= LOCAL_BOOL_TEMP_START and virtual_addr <= LOCAL_BOOL_END):
        return virtual_addr - LOCAL_BOOL_TEMP_START
    elif (virtual_addr >= CONST_INT_START and virtual_addr <= CONST_INT_END):
        return virtual_addr - CONST_INT_START
    elif (virtual_addr >= CONST_FLOAT_START and virtual_addr <= CONST_FLOAT_END):
        return virtual_addr - CONST_FLOAT_START
    elif (virtual_addr >= CONST_CHAR_START and virtual_addr <= CONST_CHAR_END):
        return virtual_addr - CONST_CHAR_START
    elif (virtual_addr >= CONST_BOOL_START and virtual_addr <= CONST_BOOL_END):
        return virtual_addr - CONST_BOOL_START
    else:
        print("Error: Virtual address out of range.")
        return -1