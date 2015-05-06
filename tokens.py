
import ply.lex as lex
from quad import *

#Globales
GLOBENTERO = 1000
GLOBDECIMAL =1500
GLOBesVerdad =2000
GLOBFRASE =2500

#Locales
LOCALENTERO =3000
LOCALDECIMAL =3500
LOCALesVerdad =4000
LOCALFRASE =4500

#Temporales
TEMPENTERO =5000
TEMPDECIMAL =5500
TEMPesVerdad =6000
TEMPFRASE =6500

#constantes
CONSTENTERO = 7000
CONSTDECIMAL = 7500 
CONSTesVerdad = 8000
CONSTFRASE= 8500

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
    'sino'    : 'SINO',
    'haz'     : 'HAZ',
    'var'	  : 'VAR'
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
    'programa : PROGRAMA ID programa_push_id var body'
    init()
    printcuadruplos()
    print(t[1])

def p_var(t):
	'''var : VAR id vars COLON tipo vars2
		 | empty'''
		 
def p_vars(t):
	'''vars : COMMA id
			| empty'''
def p_vars2(t):
	'''vars2 : var
			 | empty'''

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
	'funcion : FUNCION tipo ID funcion_push_id LPAREN funparam RPAREN LLLAVE bloque RLLAVE'
	print("funcion")

def funcion_push_id():
    'funcion_push_id: '
    #creamos espacio en memoria para la funcion
    

def p_funparam(t):
	'''funparam : tipo ID funparams
				| empty'''

def p_funparams(t):
	'''funparams : COMMA funparam
				 | empty'''
				 


def p_tipo(t):
    '''tipo : ENTERO
            | DECIMAL
            | FRASE
            | ESVERDAD'''
            
def p_estatuto(t):
	'''estatuto : asignacion bloque
				| condicion bloque
				| mientras bloque 
				| para bloque
				| escritura bloque
				| llamada bloque'''
	print("estatuto")

def p_asignacion(t):
    'asignacion : ID asignacion_push_id IGUAL asignacion_push_igual expresion'
    print("asignacion")
    assign()
    
def asignacion_push_id(t):
    'asignacion_push_id :'
    dire = t[1] #mas obtencion de memoria  
    pila_id(dire)

def asignacion_push_igual(t):
    'asignacion_push_igual :'
    pila_op(8)

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
	'''expresions : MAYOR expresions_push_mayor exp
				  | MENOR expresions_push_menor exp 
				  | COMPARA expresions_push_compara exp
				  | empty'''

def p_expresions_push_mayor(t):
    'p_expresions_push_mayor: '
    pila_op(6)

def p_expresions_push_menor(t):
    'p_expresions_push_menor: '
    pila_op(5)

def p_expresions_push_compara(t):
    'p_expresions_push_compara: '
    pila_op(7)

def p_exp(t):
	'exp : termino exps'

def p_exps(t):
	'''exps : PLUS exps_push_plus termino exps
			| MINUS exps_push_minus termino exps
			| empty'''
	print("suma/resta")

def p_exps_push_plus(t):
    'p_exps_push_plus: '
    pila_op(1)

def p_exps_push_minus(t):
    'p_exps_push_plus: '
    pila_op(2)
        
def p_termino(t):
	'termino : factor terminos'

def p_terminos(t):
	'''terminos : TIMES terminos_push_times factor terminos
				| DIVIDE terminos_push_divide factor terminos
				| empty'''
	print("multi/div")

def p_terminos_push_times(t):
    'p_terminos_push_times: '
    pila_op(3)

def p_terminos_push_divide(t):
    'p_terminos_push_divide: '
    pila_op(4)
    
def p_factor(t):
	'''factor : LPAREN factor_lparent expresion RPAREN factor_rparen
			  | valor'''

def p_factor_lparent:
    'p_factor_lparent'
    parentesisPush()

def p_factor_rparent:
    'p_factor_rparent'
    parentesisPop()

def p_valor(t):
    '''valor : ID
             | CTEINT
             | CTEDEC
             | llamada'''
    global CONSTENTERO
    global CONSTDECIMAL
    if isinstance(t[1], str):
         pila_id(1050) #direccion de T
    elif isinstance(t[1], int):
         pila_op(CONSTENTERO)
         CONSTENTERO = CONSTENTERO + 1
    elif isinstance(t[1], float):      
         pila_op(CONSTDECIMAL)
         CONSTDECIMAL = CONSTDECIMAL + 1
    
def p_condicion(t):
	'condicion : SI LPAREN expresion RPAREN condicion_if LLLAVE estatuto  RLLAVE else'
	print("condicion")

def p_condicion_if(t):
    'p_condition_if: '
    if1()

def p_else(t):
    '''else : SINO else_2 LLLAVE estatuto RLLAVE
            | empty'''
    print("else")
    if2()

def p_else_2:
    'p_else_2: '
    else1()

def p_para(t):
	'para : PARA ID ENRANGO LPAREN param COMMA param RPAREN LLLAVE estatuto RLLAVE'
	print("for")

def p_param(t):
	'''param : ID
			 | CTEINT''' 
	print("param")

def p_mientras(t):
    'mientras : HAZ  mientras_haz_push LLLAVE estatuto RLLAVE MIENTRAS LPAREN expresion RPAREN'
    print("mientras")
    do2()

def p_mientras_haz_push(t):
    'p_mientras_haz_push: '
    do1()
    
def p_escritura(t):
    'escritura : IMPRIME escritura_escribe LPAREN esc RPAREN'
    print("print")
    print2()
    
def p_escritura_escribe(t):
    'p_escritura_escribe : '
    print1()
    
def p_esc(t):
	'''esc : expresion escs
		   | STRING escs'''
	print(t[1])
def p_escs(t):
	'''escs : COMMA esc
			| empty'''	
			
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