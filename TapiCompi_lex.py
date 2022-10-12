"""
TapiCompi_lex module is a lexer for TapiCompi language.

Author: Jazmín Santibáñez
"""


from ply import *
import ply.lex as lex

# Reserved words
reserved = {
    
    ## <PROGRAMA>
    'main' : 'MAIN',
    
    ## <DEC_VAR>
    'var' : 'VAR',
    
    ## <TIPO_S>
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    
    ## <FUNCS>
    'func' : 'FUNC',
    'void' : 'VOID',
    'return' : 'RETURN',
    
    ## <ESTATUTOS> 
    'read' : 'READ',
    'print' : 'PRINT',
    
    'if' : 'IF',
    'else' : 'ELSE',
    
    'while' : 'WHILE',
    
    'for' : 'FOR',
    'to' : 'TO',
    'step' : 'STEP',
}

# Tokens
tokens = [
    # ## Reserved words
    # 'MAIN', 'VAR', 
    # 'INT', 'FLOAT', 'CHAR',
    # 'FUNC', 'VOID', 'RETURN',
    # 'READ', 'PRINT', 
    # 'IF', 'ELSE', 
    # 'WHILE', 'FOR', 'TO', 'STEP',
    
    ## Operators
    'OP_ASSIGN', 
    'OP_AND', 'OP_OR',
    'OP_ADD', 'OP_SUBTR', 'OP_MULT', 'OP_DIV',
    'OP_EQ','OP_NEQ', 'OP_LT', 'OP_GT', 'OP_LTE', 'OP_GTE',
    
    ## Separators
    'lPAREN', 'rPAREN', ## ()
    'lBRACE', 'rBRACE', ## {}
    'lBRACKET', 'rBRACKET', ## []
    'SEP_SEMICOLON', ## ;   
    'SEP_COMMA', ## ,
    
    'ID',
    'CTE_I', 'CTE_F', 'CTE_CHAR',
    'LETRERO', 'COMENTARIO',
]

tokens += reserved.values()


def Lexer():
    # Simple definitions of tokens
    t_OP_ASSIGN = r'\='

    ## Logical operators
    t_OP_AND = r'\&'
    t_OP_OR = r'\|'

    ## Arithmetic operators
    t_OP_ADD = r'\+'
    t_OP_SUBTR = r'\-'
    t_OP_MULT = r'\*'
    t_OP_DIV = r'\/'

    ## Relational operators
    t_OP_EQ = r'\=\='
    t_OP_NEQ = r'\!\='
    t_OP_LT = r'\<'
    t_OP_GT = r'\>'
    t_OP_LTE = r'\<\='
    t_OP_GTE = r'\>\='

    t_lPAREN = r'\('
    t_rPAREN = r'\)'
    t_lBRACE = r'\{'
    t_rBRACE = r'\}'
    t_lBRACKET = r'\['
    t_rBRACKET = r'\]'

    t_SEP_SEMICOLON = r'\;'
    t_SEP_COMMA = r'\,'

    t_ignore = ' \t'


    # Definition of tokens / Regular expressions
    def t_CTE_F(t):
        r'[0-9]+(\.[0-9]+)?'
        t.value = float(t.value)
        return t

    def t_CTE_I(t):
        r'[0-9]+'
        t.value = int(t.value)
        return t

    def t_CTE_CHAR(t):
        r'\'[a-zA-Z0-9]\''
        return t

    def t_LETRERO(t):
        r'(\"[^(\"|\')]*\")'
        return t

    def t_COMENTARIO(t):
        r'\#.*'
        pass

    def t_ID(t):
        r'[a-zA-Z][a-zA-Z0-9_]*'
        if t.value in reserved:
            t.type = reserved[ t.value ]
        #t.value = (t.value, symbol_lookup(t.value))
        return t

    # Rule to track line number
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        
    # Rule to manage errors
    def t_error(t):
        print("Caracter no reconocido '%s'" % t.value[0])
        t.lexer.skip(1)
    
    # Build the lexer
    return lex.lex() 