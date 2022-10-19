from enum import Enum

# enum value --> {nameClass}.{key}.value)
#  enum name --> {nameClass}(value).name

class Type(Enum):
    INT = 1
    FLOAT = 2
    CHAR = 3
    BOOL = 4
    