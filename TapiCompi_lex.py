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
tokens = (
    ## Reserved words
    'MAIN', 'VAR', 
    'INT', 'FLOAT', 'CHAR',
    'FUNC', 'VOID', 'RETURN',
    'READ', 'PRINT', 
    'IF', 'ELSE', 
    'WHILE', 'FOR', 'TO', 'STEP',
    
    ## Operators
    'OP_assign', 
    'OP_add', 'OP_sub', 'OP_mul', 'OP_div',
    'OP_eq','OP_diff', 'OP_lt', 'OP_gt',
    
    ## Separators
    'lParen', 'rParen', ## ()
    'lBrace', 'rBrace', ## {}
    'lBracket', 'rBracket', ## []
    'SEP_semicolon', ## ;   
    'SEP_comma', ## ,
    
    'ID',
    'CTE_I', 'CTE_F', 'CTE_CHAR',
    'LETRERO', 'COMENTARIO'
)


# Simple definitions of tokens
t_OP_assign = r'\='

t_OP_add = r'\+'
t_OP_sub = r'\-'
t_OP_mul = r'\*'
t_OP_div = r'\/'

t_OP_eq = r'\=\='
t_OP_diff = r'\!\='
t_OP_lt = r'\<'
t_OP_gt = r'\>'

t_lParen = r'\('
t_rParen = r'\)'
t_lBrace = r'\{'
t_rBrace = r'\}'
t_lBracket = r'\['
t_rBracket = r'\]'

t_SEP_semicolon = r'\;'
t_SEP_comma = r'\,'

t_ignore = ' \t'


# Definition of tokens / Regular expressions
def t_CTE_F(t):
    r'[0-9]+\.[0-9]+'
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
    r'("[^\"]*")'
    return t

def t_COMENTARIO(t):
    r'\#.*'
    pass

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Rule to track line number
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
# Rule to manage errors
def t_error(t):
    print("Caracter no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)