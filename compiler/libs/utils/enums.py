from enum import Enum

# enum value --> {nameClass}.{key}.value)
#                   Type[varKey].value
#  enum name --> {nameClass}(value).name

class Type(Enum):
    '''
    Enum to map the types of the variables
    * INT - 1
    * FLOAT - 2
    * CHAR - 3
    * BOOL - 4
    '''
    INT = 1
    FLOAT = 2
    CHAR = 3
    BOOL = 4