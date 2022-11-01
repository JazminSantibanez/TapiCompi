# Path: TapiCompi\compiler\libs\CuboSem.py

import numpy as np
import pandas as pd


# Do: Change types for enums


dict_MultDiv = {
    'int' : {'int': 'int', 'float': 'int'},
    'float': {'int': 'int', 'float': 'float'},
}

dict_SumRes = {
    'int': {'int': 'int', 'float': 'float'},
    'float': {'int': 'float', 'float': 'float'},
}

dict_Relacionales = {
    'int': {'int': 'bool', 'float': 'bool'},
    'float': {'int': 'bool', 'float': 'bool'},
}

dict_EqDes = dict_Relacionales.copy()
dict_EqDes['bool'] = {'bool': 'bool'}
dict_EqDes['char'] = {'char': 'bool'}

dict_Logicos = {
    'bool': {'bool': 'bool'},
}

dict_SameType = {
    'int': {'int': 'int'},
    'float': {'float': 'float'},
    'bool': {'bool': 'bool'},
    'char': {'char': 'char'}
}

# Create semantic cube for operations between types of variables

Cubo_Sem = {
    # Arithmetic operators
    '*': dict_MultDiv,
    '/': dict_MultDiv,
    '+': dict_SumRes,
    '-': dict_SumRes,

    # Relational operators
    '>': dict_Relacionales,
    '<': dict_Relacionales,
    '>=': dict_Relacionales,
    '<=': dict_Relacionales,
    '==': dict_EqDes,
    '!=': dict_EqDes,

    # Logic operators
    '&': dict_Logicos,
    '|': dict_Logicos,
    
    # Asssign
    '=': dict_SameType
}

df_cuboSem = pd.DataFrame(Cubo_Sem)

# Access the type_res of an expression
# df_cuboSem['==']['bool']['bool']

def validate_type(
    operator, 
    typeL : str, 
    typeR : str) -> str:
    '''
    Function that checks if the operation between two types is valid.
    
    Args:
        operator (char): Operator of the operation.
        typeL (Type): Type of the left operand.
        typeR (Type): Type of the right operand.
        
    Returns:
        Type: Type of the result of the operation.
        -1 if the operation is not valid.
    '''
    try:
        type_res = df_cuboSem[operator][typeL][typeR]
        return type_res
    except:
        return -1 # Error code to handle mismatched types
    
