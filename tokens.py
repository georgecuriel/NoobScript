
import ply.lex as lex
from quad import *

#Globales
GLOBENTERO = 1000
GLOBDECIMAL =1500
GLOBESVERDAD =2000
GLOBFRASE =2500

#Locales
LOCALENTERO =3000
LOCALDECIMAL =3500
LOCALESVERDAD =4000
LOCALFRASE =4500

#Temporales
TEMPENTERO =5000
TEMPDECIMAL =5500
TEMPESVERDAD =6000
TEMPFRASE =6500

#constantes
CONSTENTERO = 7000
CONSTDECIMAL = 7500 
CONSTESVERDAD = 8000
CONSTFRASE= 8500

#directorio de procs y tablas de variables y constantes
#listas de [nombre, tipo, cuadinicio, {}param, {}vars]
directorio = []
func = 0
directorioconst = {}
direccion = 0
funnombre = ''
funtipo = ''
funcuad = 1
funparam = {}
funvars = {}

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
    'programa : PROGRAMA ID programa_push_id vars programa_push_dict body'
    #init()
    #printcuadruplos()
    global directorio
    print(t[1])
    print directorio
    print ('termine')

def p_programa_push_id(t):
	'programa_push_id : '
	global funnombre
	funnombre = t[-1]

def p_programa_push_dict(t):
	'programa_push_dict : '
	global diccionario
	directorio.append(list((funnombre, funtipo, funcuad, funparam, funvars)))
		

def p_vars(t):
	'''vars : VAR vars2
			 | empty'''

def p_vars2(t):
	'vars2 : tipo ID vars_push_id vars3 SEMICOL vars4'
	
def p_vars_push_id(t):
	'vars_push_id : '
	global directorio
	global direccion
	global funvars
	funvars[t[-1]] = direccion
	
	
def p_vars3(t):
	'''vars3 : COMMA ID vars3_push_id vars3
			 | empty'''

def p_vars3_push_id(t):
	'vars3_push_id : '
	global direccion
	global funvars
	funvars[t[-1]] = direccion
	
			 
def p_vars4(t):
	'''vars4 : vars2
			 | empty'''


def p_tipo(t):
	'''tipo : ENTERO
			| DECIMAL
			| FRASE
			| ESVERDAD'''
	global direccion
	global GLOBENTERO
	global LOCALENTERO
	global GLOBDECIMAL
	global LOCALDECIMAL
	global GLOBESVERDAD
	global LOCALESVERDAD
	global GLOBFRASE
	global LOCALFRASE
	if t[1] == 'entero':
		if func == 0:
			GLOBENTERO += GLOBENTERO 
			direccion = GLOBENTERO
		else:
			LOCALENTERO +=1
			direccion = LOCALENTERO
	elif t[1] == 'decimal':
		if func == 0:
			GLOBDECIMAL +=1
			direccion = GLOBDECIMAL
		else:
			LOCALDECIMAL +=1
			direccion = LOCALDECIMAL
	elif t[1] == 'esVerdad':
		if func == 0:
			GLOBESVERDAD +=1
			direccion = GLOBESVERDAD
		else:
			LOCALESVERDAD +=1
			direccion = LOCALESVERDAD
	elif t[1] == 'frase':
		if func == 0:
			BLOBFRASE +=1
			direccion = GLOBFRASE
		else:
			LOCALFRASE +=1
			direccion = LOCALFRASE
	
			

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
	'funcion : FUNCION funcion_increase_func tipo ID funcion_push_id LPAREN funparam RPAREN LLLAVE vars bloque RLLAVE'
	print("funcion")

def p_funcion_increase_func(t):
	'funcion_increase_func : '
	global directorio
	global func
	func += 1
	directorio[func][4] = {}

def p_funcion_push_id(t):
    'funcion_push_id : '
    #creamos espacio en memoria para la funcion
    

def p_funparam(t):
	'''funparam : tipo ID funparams
				| empty'''

def p_funparams(t):
	'''funparams : COMMA funparam
				 | empty'''
            
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
    
def p_asignacion_push_id(t):
    'asignacion_push_id :'
    dire = t[1] #mas obtencion de memoria  
    pila_id(dire)

def p_asignacion_push_igual(t):
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
    'expresions_push_mayor : '
    pila_op(6)

def p_expresions_push_menor(t):
    'expresions_push_menor : '
    pila_op(5)

def p_expresions_push_compara(t):
    'expresions_push_compara : '
    pila_op(7)

def p_exp(t):
	'exp : termino exps'

def p_exps(t):
	'''exps : PLUS exps_push_plus termino exps
			| MINUS exps_push_minus termino exps
			| empty'''
	print("suma/resta")

def p_exps_push_plus(t):
    'exps_push_plus : '
    pila_op(1)

def p_exps_push_minus(t):
    'exps_push_minus : '
    pila_op(2)
        
def p_termino(t):
	'termino : factor terminos'

def p_terminos(t):
	'''terminos : TIMES terminos_push_times factor terminos
				| DIVIDE terminos_push_divide factor terminos
				| empty'''
	print("multi/div")

def p_terminos_push_times(t):
    'terminos_push_times : '
    pila_op(3)

def p_terminos_push_divide(t):
    'terminos_push_divide : '
    pila_op(4)
    
def p_factor(t):
	'''factor : LPAREN factor_lparen expresion RPAREN factor_rparen
			  | valor'''

def p_factor_lparent(t):
    'factor_lparen : '
    parentesisPush()

def p_factor_rparent(t):
    'factor_rparen : '
    parentesisPop()

def p_valor(t):
    '''valor : ID
             | CTEINT
             | CTEDEC
             | llamada'''
    global CONSTENTERO
    global CONTSTDECILMAL
    global CONSTDECIMAL
    global CONSTESVERDAD
    global CONSTFRASE
    global direccion
	global GLOBENTERO
	global LOCALENTERO
	global GLOBDECIMAL
	global LOCALDECIMAL
	global GLOBESVERDAD
	global LOCALESVERDAD
	global GLOBFRASE
	global LOCALFRASE
  

    if isinstance(t[1], int):      
		if t[1] in directorioconst: 
			pila_id(directorioconst[t[1]])
		else:
			CONSTENTERO += 1
			directorioconst[t[1]] = CONSTENTERO
			pila_id(directorioconst[t[1]])
    elif isinstance(t[1], float):      
		if t[1] in directorioconst:
			pila_id(directorioconst[t[1]])
		else:
			CONSTDECIMAL += 1
			directorioconst[t[1]] = CONSTDECIMAL
			pila_id(directorioconst[t[1]])
    elif isinstance(t[1], str):      #checar global y func
		if t[1] in funvars[t[1]]:
			pila_id(funvars[t[1]])
		else
			

def p_condicion(t):
	'condicion : SI LPAREN expresion RPAREN condicion_if LLLAVE estatuto  RLLAVE else'
	print("condicion")

def p_condicion_if(t):
    'condicion_if : '
    if1()

def p_else(t):
    '''else : SINO else_2 LLLAVE estatuto RLLAVE
            | empty'''
    print("else")
    if2()

def p_else_2(t):
    'else_2 : '
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
    'mientras_haz_push : '
    do1()
    
def p_escritura(t):
    'escritura : IMPRIME escritura_escribe LPAREN esc RPAREN'
    print("print")
    print2()
    
def p_escritura_escribe(t):
    'escritura_escribe : '
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