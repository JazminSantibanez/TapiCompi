import numpy as np
from libs.Address_Manager import *
from libs.utils.Constants import *

class Memory:
    def __init__(self, li, lf, lc, lb, ti, tf, tc, tb):
        self.local_int = np.zeros(li, dtype=np.int64)
        self.local_float = np.zeros(lf, dtype=float)
        self.local_char = np.zeros(lc, dtype="U1")
        self.local_bool = np.zeros(lb, dtype=bool)
        
        self.temp_int = np.zeros(ti, dtype=np.int64)
        self.temp_float = np.zeros(tf, dtype=float)
        self.temp_char = np.zeros(tc, dtype="U1")
        self.temp_bool = np.zeros(tb, dtype=bool)
        
    def set_value_local(self, virtual_address, value):
        index = get_Memory_Index(virtual_address)
        
        # Local/Global variables        
        if ((virtual_address >= GLOBAL_INT_START and virtual_address <= GLOBAL_INT_END) or 
            (virtual_address >= LOCAL_INT_START and virtual_address < LOCAL_INT_TEMP_START)):
            self.local_int[index] = value
        elif ((virtual_address >= GLOBAL_FLOAT_START and virtual_address <= GLOBAL_FLOAT_END) or 
              (virtual_address >= LOCAL_FLOAT_START and virtual_address < LOCAL_FLOAT_TEMP_START)):
            self.local_float[index] = value
        elif ((virtual_address >= GLOBAL_CHAR_START and virtual_address <= GLOBAL_CHAR_END) or 
              (virtual_address >= LOCAL_CHAR_START and virtual_address < LOCAL_CHAR_TEMP_START)):
            self.local_char[index] = value
        elif ((virtual_address >= GLOBAL_BOOL_START and virtual_address <= GLOBAL_BOOL_END) or 
              (virtual_address >= LOCAL_BOOL_START and virtual_address < LOCAL_BOOL_TEMP_START)):
            self.local_bool[index] = value
        # Temporal variables
        elif ((virtual_address >= LOCAL_INT_TEMP_START and virtual_address <= LOCAL_INT_END)):
            self.temp_int[index] = value
        elif ((virtual_address >= LOCAL_FLOAT_TEMP_START and virtual_address <= LOCAL_FLOAT_END)):
            self.temp_float[index] = value
        elif ((virtual_address >= LOCAL_CHAR_TEMP_START and virtual_address <= LOCAL_CHAR_END)):
            self.temp_char[index] = value
        elif ((virtual_address >= LOCAL_BOOL_TEMP_START and virtual_address <= LOCAL_BOOL_END)):
            self.temp_bool[index] = value
            
    def get_value_local(self, virtual_address):
        index = get_Memory_Index(virtual_address)
         # Local/Global variables        
        if ((virtual_address >= GLOBAL_INT_START and virtual_address <= GLOBAL_INT_END) or 
            (virtual_address >= LOCAL_INT_START and virtual_address < LOCAL_INT_TEMP_START)):
            return self.local_int[index] 
        elif ((virtual_address >= GLOBAL_FLOAT_START and virtual_address <= GLOBAL_FLOAT_END) or 
              (virtual_address >= LOCAL_FLOAT_START and virtual_address < LOCAL_FLOAT_TEMP_START)):
            return self.local_float[index]
        elif ((virtual_address >= GLOBAL_CHAR_START and virtual_address <= GLOBAL_CHAR_END) or 
              (virtual_address >= LOCAL_CHAR_START and virtual_address < LOCAL_CHAR_TEMP_START)):
            return self.local_char[index]
        elif ((virtual_address >= GLOBAL_BOOL_START and virtual_address <= GLOBAL_BOOL_END) or 
              (virtual_address >= LOCAL_BOOL_START and virtual_address < LOCAL_BOOL_TEMP_START)):
            return self.local_bool[index]
        # Temporal variables
        elif ((virtual_address >= LOCAL_INT_TEMP_START and virtual_address <= LOCAL_INT_END)):
            return self.temp_int[index]
        elif ((virtual_address >= LOCAL_FLOAT_TEMP_START and virtual_address <= LOCAL_FLOAT_END)):
            return self.temp_float[index]
        elif ((virtual_address >= LOCAL_CHAR_TEMP_START and virtual_address <= LOCAL_CHAR_END)):
            return self.temp_char[index]
        elif ((virtual_address >= LOCAL_BOOL_TEMP_START and virtual_address <= LOCAL_BOOL_END)):
            return self.temp_bool[index]