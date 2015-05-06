    # ------------------------------------------------------------
    # 
    #
    # 
    # 
    # ------------------------------------------------------------
import ply.lex as lex

reserved = {
	'entero'  : 'ENTERO',
	'decimal' : 'DECIMAL',
	'frase'   : 'FRASE',
	'imprime' : 'IMPRIME',
	'lee'     : 'LEE',
	'clase'   : 'CLASE',
	'vGlobal' : 'VGLOBAL',
	'esVerdad': 'ESVERDAD',
	'programa': 'PROGRAMA',
	'funcion' : 'FUNCION',
	'enRango' : 'ENRANGO',
	'para'    : 'PARA',
	'mientras': 'MIENTRAS',
	'si'      : 'SI',
	'sino'    : 'SINO'
}

    # List of token names.   This is always required
tokens = [
    'CTEDEC',
    'CTEINT',
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
    'ID',
    'COMMA',
    'COLON',
    'SEMICOL',
    'STRING',
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
t_COMMA    = r','
t_COLON    = r':'
t_SEMICOL  = r';'

def t_STRING(t):
	r'\'(\s*\w)*\''
	return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t
    
    # A regular expression for floats
def t_CTEDEC(t):
    r'\d+\.\d+'
    t.value = float(t.value)    
    return t    
    
    # A regular expression for integers
def t_CTEINT(t):
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
data = '''2*4+5(4/2.4)<=[{]}= == si no hay mientras sino 'brodi como esta'
#hola adios
a d entero frase
imprime('fuentes del valle')
programa patito funcion id (entero a, entero b){c=2+3}'''

    # Give the lexer some input
lexer.input(data)
 
    # Tokenize
for tok in lexer:
	print tok

#parsing rules
precedence = (
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE'),
)

def p_programa(t):
	'programa : PROGRAMA ID body'
	print(t[1])

def p_empty(t):
	'empty : '
	
def p_body(t):
	'''body : funcion body
			| bloque body
			| empty'''
			
def p_bloque(t):
	'''bloque : estatuto
			  | empty'''
			  
def p_funcion(t):
	'funcion : FUNCION ID LPAREN funparam RPAREN LLLAVE bloque RLLAVE'
	print("funcion")

def p_funparam(t):
	'''funparam : tipo ID funparams
				| empty'''

def p_funparams(t):
	'''funparams : COMMA funparam
				 | empty'''
				 
def p_tipo(t):
	'''tipo : ENTERO
			| DECIMAL
			| FRASE'''
	 
def p_estatuto(t):
	'''estatuto : asignacion bloque
				| condicion bloque
				| mientras bloque 
				| para bloque
				| escritura bloque
				| llamada bloque'''
	print("estatuto")

def p_asignacion(t):
	'asignacion : ID IGUAL expresion'
	print("asignacion")

def p_llamada(t):
	'llamada : ID LPAREN llamadaparam RPAREN'

def p_llamadaparam(t):
	'''llamadaparam : valor llamadaparams
					| empty'''

def p_llamadaparams(t):
	'''llamadaparams : COMMA llamadaparam
					 | empty'''
		
	

def p_expresion(t):
	'''expresion : exp expresions
		  		 | LEE LPAREN STRING RPAREN SEMICOL'''
	print("expresion")
		  		
def p_expresions(t):
	'''expresions : MAYOR exp
				  | MENOR exp
				  | COMPARA exp
				  | empty'''

def p_exp(t):
	'exp : termino exps'

def p_exps(t):
	'''exps : PLUS termino exps
			| MINUS termino exps
			| empty'''
	print("suma/resta")
			
def p_termino(t):
	'termino : factor terminos'

def p_terminos(t):
	'''terminos : TIMES factor terminos
				| DIVIDE factor terminos
				| empty'''
	print("multi/div")
				
def p_factor(t):
	'''factor : LPAREN expresion RPAREN
			  | valor'''

def p_valor(t):
	'''valor : ID
			 | CTEINT
			 | CTEDEC'''

def p_condicion(t):
	'condicion : SI LPAREN expresion RPAREN LLLAVE estatuto  RLLAVE else'
	print("condicion")
	
def p_else(t):
	'''else : SINO LLLAVE estatuto RLLAVE
			| empty'''
	print("else")

def p_para(t):
	'para : PARA ID ENRANGO LPAREN param COMMA param RPAREN LLLAVE estatuto RLLAVE'
	print("for")

def p_param(t):
	'''param : ID
			 | CTEINT''' 
	print("param")
			 
def p_mientras(t):
	'mientras : MIENTRAS LPAREN expresion RPAREN LLLAVE estatuto RLLAVE'
	print("mientras")
	
def p_escritura(t):
	'escritura : IMPRIME LPAREN esc RPAREN'
	print("print")
	
def p_esc(t):
	'''esc : expresion escs
		   | STRING escs'''
	print(t[1])
def p_escs(t):
	'''escs : COMMA esc
			| empty'''	
	print("print2")
			
def p_error(t):
    print("Syntax error at '%s'" % t.value)
			
import ply.yacc as yacc
parser = yacc.yacc()


			
while True:
   try:
       s = raw_input('tokens >')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)