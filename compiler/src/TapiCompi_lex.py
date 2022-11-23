#
# TapiCompi_lex module is a lexer for TapiCompi language.
#
# Author: Jazmín Santibáñez
#


from src.ply import *
import src.ply.lex as lex

# Reserved words
reserved = {
    
    ## <PROGRAMA>
    'program' : 'PROGRAM',
    'main' : 'MAIN',
    
    ## <DEC_VAR>
    'var' : 'VAR',
    
    ## <TIPO_S>
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    'bool' : 'BOOL',
    
    ## <TIPO_C>
    'dataframe' : 'DATAFRAME',
    'file' : 'FILE',
    
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
    'do' : 'DO',
    
}

# Tokens
tokens = [
        
    ## Operators
    'OP_ASSIGN', 
    'OP_AND', 'OP_OR',
    'OP_ADD', 'OP_SUBTR', 'OP_MULT', 'OP_DIV',
    'OP_EQ','OP_NEQ', 'OP_LT', 'OP_GT', 'OP_LTE', 'OP_GTE',
    
    ## Separators
    'lPAREN', 'rPAREN', ## ()
    'lBRACE', 'rBRACE', ## {}
    'lBRACKET', 'rBRACKET', ## []
    #'SEP_SEMICOLON', ## ;   
    'SEP_COMMA', ## ,
    'SEP_COLON', ## :
    
    'ID',
    'CTE_F', 'CTE_I', 'CTE_CHAR',
    'LETRERO', 'COMENTARIO',
]

tokens += reserved.values()

# Simple definitions of tokens
t_OP_ASSIGN = r'='

## Logical operators
t_OP_AND = r'&'
t_OP_OR = r'\|'

## Arithmetic operators
t_OP_ADD = r'\+'
t_OP_SUBTR = r'-'
t_OP_MULT = r'\*'
t_OP_DIV = r'/'

## Relational operators
t_OP_EQ = r'=='
t_OP_NEQ = r'!='
t_OP_LT = r'<'
t_OP_GT = r'>'
t_OP_LTE = r'<='
t_OP_GTE = r'>='

t_lPAREN = r'\('
t_rPAREN = r'\)'
t_lBRACE = r'\{'
t_rBRACE = r'\}'
t_lBRACKET = r'\['
t_rBRACKET = r'\]'

#t_SEP_SEMICOLON = r';'
t_SEP_COMMA = r','
t_SEP_COLON = r'\:'

t_ignore = ' \t' # Ignore spaces and tabs


# Definition of tokens / Regular expressions

def t_COMENTARIO(t):
    r'\#.*'
    pass # Token discarded

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID') # Check if it is a reserved word
    #t.value = (t.value, symbol_lookup(t.value))
    return t

def t_CTE_F(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CTE_I(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

def t_CTE_CHAR(t):
    r'\'[a-zA-Z]\''
    return t

def t_LETRERO(t):
    r'"[^"]*"'
    return t


# Rule to track line number
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
# Rule to manage errors
def t_error(t):
    print("Caracter no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

def Tokenize(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: break
        print(tok)
 
# Build the lexer
lexer = lex.lex()

