

    # ------------------------------------------------------------
    # calclex.py
    #
    # tokenizer for a simple expression evaluator for
    # numbers and +,-,*,/
    # ------------------------------------------------------------
import ply.lex as lex

reserved = {
	'palabra' : 'PALABRA',
	'entero'  : 'ENTERO',
	'decimal' : 'DECIMAL',
	'frase'   : 'FRASE',
	'imprime' : 'IMPRIME',
	'lee'     : 'LEE',
	'clase'   : 'CLASE',
	'vGlobal' : 'VGLOBAL',
	'esVerdad': 'ESVERDAD',
	'programa': 'PROGRAMA',
	'funcion' : 'FNUNCION',
	'enRango' : 'ENRANGO',
	'ciclo'   : 'CICLO',
	'mientras': 'MIENTRAS',
	'si'      : 'SI',
	'sino'    : 'SINO'
}

    # List of token names.   This is always required
tokens = [
    'DECIMAL',
    'ENTERO',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'MAYOR',
    'MENOR',
    'IGUAL',
    'COMPARA',
    'LBRAK',
    'RBRAK',
    'LLLAVE',
    'RLLAVE',
    'ID'
] + list(reserved.values())

    # Regular expression rules for simple tokens
t_PLUS     = r'\+'
t_MINUS    = r'-'
t_TIMES    = r'\*'
t_DIVIDE   = r'/'
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_MAYOR    = r'<'
t_MENOR    = r'>'
t_IGUAL    = r'='
t_COMPARA  = r'=='
t_LBRAK    = r'\['
t_RBRAK    = r'\]'
t_LLLAVE   = r'{'
t_RLLAVE   = r'}'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t
    
    # A regular expression for floats
def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)    
    return t    
    
    # A regular expression for integers
def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)    
    return t

	
    # Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

#discard comments
def t_COMMENT(t):
	r'\#.*'
	pass

    # Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

    # Build the lexer
lexer = lex.lex()

    # Test it out
data = '''2*4+5(4/2.4)<=[{]}= == si no hay mientras sino
#hola adios
a d 
'''

    # Give the lexer some input
lexer.input(data)

    # Tokenize
for tok in lexer:
	print tok

#parsing rules
precedence = (
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE'),
	('right','UMINUS'),
)

def p_programa(t):
	'programa : PROGRAMA ID bloque'

def p_empty(t):
	'empty:'
	pass
	
def p_bloque(t):
	'''bloque : empty
			  | estatuto'''
			  
def p_estatuto(t):
	'''estatuto : asignacion bloque
				| condicion bloque
				| ciclo bloque 
				| escritura bloque
				| funcion bloque 
				| clase bloque'''

def p_asignacion(t):
	'asignacion : ID IGUAL expresion'
	

def p_expresion(t):
	
