import numpy as np
import pandas as pd

dict_MultDiv = {
    'int': {'int': 'int', 'float': 'int'},
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

# Creacion de un dataframe para almacenar los tipos de datos

cuboSem = {
    # Operadores aritmeticos
    '*': dict_MultDiv,
    '/': dict_MultDiv,
    '+': dict_SumRes,
    '-': dict_SumRes,

    # Operadores relacionales
    '>': dict_Relacionales,
    '<': dict_Relacionales,
    '>=': dict_Relacionales,
    '<=': dict_Relacionales,
    '==': dict_EqDes,
    '!=': dict_EqDes,

    # Operadores logicos
    '&': dict_Logicos,
    '|': dict_Logicos,
}

df_cuboSem = pd.DataFrame(cuboSem)

# Access the type_res of an expression
# df_cuboSem['==']['bool']['bool'])

def validate_type(operator, typeL, typeR):
    try:
        type_res = df_cuboSem[operator][typeL][typeR]
        return type_res
    except:
        return -1 # Error code to handle mismatched types