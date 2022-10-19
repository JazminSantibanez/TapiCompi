# Path: TapiCompi\compiler\libs\CuboSem.py

import numpy as np
import pandas as pd
from enums import Type


dict_MultDiv = {
    Type.INT : {Type.INT: Type.INT, Type.FLOAT: Type.INT},
    Type.FLOAT: {Type.INT: Type.INT, Type.FLOAT: Type.FLOAT},
}

dict_SumRes = {
    Type.INT: {Type.INT: Type.INT, Type.FLOAT: Type.FLOAT},
    Type.FLOAT: {Type.INT: Type.FLOAT, Type.FLOAT: Type.FLOAT},
}

dict_Relacionales = {
    Type.INT: {Type.INT: Type.BOOL, Type.FLOAT: Type.BOOL},
    Type.FLOAT: {Type.INT: Type.BOOL, Type.FLOAT: Type.BOOL},
}

dict_EqDes = dict_Relacionales.copy()
dict_EqDes[Type.BOOL] = {Type.BOOL: Type.BOOL}
dict_EqDes[Type.CHAR] = {Type.CHAR: Type.BOOL}

dict_Logicos = {
    Type.BOOL: {Type.BOOL: Type.BOOL},
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
}

df_cuboSem = pd.DataFrame(Cubo_Sem)

# Access the type_res of an expression
# df_cuboSem['=='][Type.BOOL][Type.BOOL]

def validate_type(operator, typeL, typeR):
    try:
        type_res = df_cuboSem[operator][typeL][typeR]
        return type_res
    except:
        return -1 # Error code to handle mismatched types
    
