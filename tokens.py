
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
funparam = []
funvars = []
#dimension de arreglo 1 var 2 array 3 matriz
dim = 0
#valor dim 1
dim1 = None
#valor dim 2
dim2 = None
#toma casilla 1 de array/matrix
llamadim1 = None
#toma casilla 2 de matrix
llamadim2 = None
#1 entero, 2 decimal, 3 esverdad, 4 frase
#tipo para definicion actual de variable
tipoactual = 0
#contador del parametro actual
paramactual = 0
#nombre de la funcion si no es variable/constante/param
nombrefunc = ''
#direccion resultado de exp
dirvalor = None
#direccion de la funcion
dirfuncion = None
init()

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
    'var'	  : 'VAR',
    'regresa' : 'REGRESA'
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
    'programa : PROGRAMA ID LLLAVE programa_push_id vars programa_push_dict body RLLAVE'
    global directorio
    global directorioconst
    print(t[1])
    print directorio
    with open('constantes.txt', 'w') as f:
        for valor, direccion in directorioconst.items():
            f.write(repr(valor))
            f.write(' ')
            f.write(repr(direccion))
            f.write('\n')
    printcuadruplos()


def p_programa_push_id(t):
    'programa_push_id : '
    global funnombre
    funnombre = t[-2]

def p_programa_push_dict(t):
    'programa_push_dict : '
    global diccionario
    global funvars
    directorio.append(list((funnombre, funtipo, funcuad, [], funvars)))
    funvars = []


def p_vars(t):
    '''vars : VAR vars2
            | empty'''

def p_vars2(t):
    'vars2 : tipo ID dimension vars_push_id vars3 SEMICOL vars4'
    
def p_dimension(t):
	'''dimension : LBRAK CTEINT push_dim1 RBRAK dimension2
				 | empty'''

def p_push_dim1(t):
    'push_dim1 : '
    global dim
    global dim1
    dim = 1
    dim1 = t[-1]
        

def p_dimension2(t):
	'''dimension2 : LBRAK CTEINT push_dim2 RBRAK
				  | empty'''

def p_push_dim2(t):
    'push_dim2 : '
    global dim
    global dim2
    dim = 2
    dim2 = t[-1]

def p_vars_push_id(t):
    'vars_push_id : '
    global directorio
    global direccion
    global funvars
    global tipoactual
    global GLOBENTERO
    global GLOBDECIMAL
    global GLOBESVERDAD
    global GLOBFRASE
    global LOCALENTERO
    global LOCALDECIMAL
    global LOCALESVERDAD
    global LOCALFRASE
    global dim
    global dim1
    global dim2
    if func == 0:
        if tipoactual == 1:
            if dim == 0:
                GLOBENTERO += 1
                funvars.append((t[-2], 0, GLOBENTERO, dim, dim1, dim2))
            elif dim == 1:
                for x in range(dim1+1):
                    GLOBENTERO += 1
                    funvars.append((t[-2], 0, GLOBENTERO, dim, dim1, dim2))
                dim1 = None
            elif dim == 2:
                for x in range(dim1+1):
                    for y in range(dim2+1):
                        GLOBENTERO += 1
                        funvars.append((t[-2], 0, GLOBENTERO, dim,dim1, dim2))
                dim1 = None
                dim2 = None
        elif tipoactual == 2:
            if dim == 0:
                GLOBDECIMAL += 1
                funvars.append((t[-2], 0, GLOBDECIMAL, dim, dim1, dim2))
            elif dim == 1:
                for x in range(dim1+1):
                    GLOBDECIMAL += 1
                    funvars.append((t[-2], 0, GLOBDECIMAL, dim, dim1, dim2))
                dim1 = None
            elif dim == 2:
                for x in range(dim1+1):
                    for y in range(dim2+1):
                        GLOBDECIMAL += 1
                        funvars.append((t[-2], 0, GLOBDECIMAL, dim, dim1, dim2))
                dim1 = None
                dim2 = None
        elif tipoactual == 3:
            if dim == 0:
                GLOBESVERDAD += 1
                funvars.append((t[-2], 0, GLOBESVERDAD, dim, dim1, dim2))
            elif dim == 1:
                for x in range(dim1+1):
                    GLOBDECIMAL += 1
                    funvars.append((t[-2], 0, GLOBESVERDAD, dim, dim1, dim2))
                dim1 = None
            elif dim == 2:
                for x in range(dim1+1):
                    for y in range(dim2+1):
                        GLOBDECIMAL += 1
                        funvars.append((t[-2], 0, GLOBESVERDAD, dim, dim1, dim2))
                dim1 = None
                dim2 = None
        elif tipoactual == 4:
            if dim == 0:
                GLOBFRASE += 1
                funvars.append((t[-2], 0, GLOBFRASE, dim, dim1, dim2))
            elif dim == 1:
                for x in range(dim1+1):
                    GLOBFRASE += 1
                    funvars.append((t[-2], 0, GLOBFRASE, dim, dim1, dim2))
                dim1 = None
            elif dim == 2:
                for x in range(dim1+1):
                    for y in range(dim2+1):
                        GLOBFRASE += 1
                        funvars.append((t[-2], 0, GLOBFRASE, dim, dim1, dim2))
                dim1 = None
                dim2 = None
    else:
        if tipoactual == 1:
            if dim == 0:
                LOCALENTERO += 1
                funvars.append((t[-2], 0, LOCALENTERO, dim, dim1, dim2))
            elif dim == 1:
                for x in range(dim1+1):
                    LOCALENTERO += 1
                    funvars.append((t[-2], 0, LOCALENTERO, dim, dim1, dim2))
                dim1 = None
            elif dim == 2:
                for x in range(dim1+1):
                    for y in range(dim2+1):
                        LOCALENTERO += 1
                        funvars.append((t[-2], 0, LOCALENTERO, dim, dim1, dim2))
                dim1 = None
                dim2 = None
        elif tipoactual == 2:
            if dim == 0:
                LOCALDECIMAL += 1
                funvars.append((t[-2], 0, LOCALDECIMAL, dim, dim1, dim2))
            elif dim == 1:
                for x in range(dim1+1):
                    LOCALDECIMAL += 1
                    funvars.append((t[-2], 0, LOCALDECIMAL, dim, dim1, dim2))
                dim1 = None
            elif dim == 2:
                for x in range(dim1+1):
                    for y in range(dim2+1):
                        LOCALDECIMAL += 1
                        funvars.append((t[-2], 0, LOCALDECIMAL, dim, dim1, dim2))
                dim1 = None
                dim2 = None
        elif tipoactual == 3:
            if dim == 0:
                LOCALESVERDAD += 1
                funvars.append((t[-2], 0, LOCALESVERDAD, dim, dim1, dim2))
            elif dim == 1:
                for x in range(dim1+1):
                    LOCALESVERDAD += 1
                    funvars.append((t[-2], 0, LOCALESVERDAD, dim, dim1, dim2))
                dim1 = None
            elif dim == 2:
                for x in range(dim1+1):
                    for y in range(dim2+1):
                        LOCALESVERDAD += 1
                        funvars.append((t[-2], 0, LOCALESVERDAD, dim, dim1, dim2))
                dim1 = None
                dim2 = None
        elif tipoactual == 4:
            if dim == 0:
                LOCALFRASE += 1
                funvars.append((t[-2], 0, LOCALFRASE, dim, dim1, dim2))
            elif dim == 1:
                for x in range(dim1+1):
                    LOCALFRASE += 1
                    funvars.append((t[-2], 0, LOCALFRASE, dim, dim1, dim2))
                dim1 = None
            elif dim == 2:
                for x in range(dim1+1):
                    for y in range(dim2+1):
                        LOCALFRASE += 1
                        funvars.append((t[-2], 0, LOCALFRASE, dim, dim1, dim2))
                dim1 = None
                dim2 = None
    dim = 0
    
def p_vars3(t):
    '''vars3 : COMMA ID dimension vars3_push_id vars3
             | empty'''

def p_vars3_push_id(t):
    'vars3_push_id : '
    global directorio
    global direccion
    global funvars
    global tipoactual
    global GLOBENTERO
    global GLOBDECIMAL
    global GLOBESVERDAD
    global GLOBFRASE
    global LOCALENTERO
    global LOCALDECIMAL
    global LOCALESVERDAD
    global LOCALFRASE
    global dim
    global dim1
    global dim2
    if func == 0:
        if tipoactual == 1:
            if dim == 0:
                GLOBENTERO += 1
                funvars.append((t[-2], 0, GLOBENTERO, dim, dim1, dim2))
            elif dim == 1:
                for x in range(dim1+1):
                    GLOBENTERO += 1
                    funvars.append((t[-2], 0, GLOBENTERO, dim, dim1, dim2))
                dim1 = None
            elif dim == 2:
                for x in range(dim1+1):
                    for y in range(dim2+1):
                        GLOBENTERO += 1
                        funvars.append((t[-2], 0, GLOBENTERO, dim,dim1, dim2))
                dim1 = None
                dim2 = None
        elif tipoactual == 2:
            if dim == 0:
                GLOBDECIMAL += 1
                funvars.append((t[-2], 0, GLOBDECIMAL, dim, dim1, dim2))
            elif dim == 1:
                for x in range(dim1+1):
                    GLOBDECIMAL += 1
                    funvars.append((t[-2], 0, GLOBDECIMAL, dim, dim1, dim2))
                dim1 = None
            elif dim == 2:
                for x in range(dim1+1):
                    for y in range(dim2+1):
                        GLOBDECIMAL += 1
                        funvars.append((t[-2], 0, GLOBDECIMAL, dim, dim1, dim2))
                dim1 = None
                dim2 = None
        elif tipoactual == 3:
            if dim == 0:
                GLOBESVERDAD += 1
                funvars.append((t[-2], 0, GLOBESVERDAD, dim, dim1, dim2))
            elif dim == 1:
                for x in range(dim1+1):
                    GLOBDECIMAL += 1
                    funvars.append((t[-2], 0, GLOBESVERDAD, dim, dim1, dim2))
                dim1 = None
            elif dim == 2:
                for x in range(dim1+1):
                    for y in range(dim2+1):
                        GLOBDECIMAL += 1
                        funvars.append((t[-2], 0, GLOBESVERDAD, dim, dim1, dim2))
                dim1 = None
                dim2 = None
        elif tipoactual == 4:
            if dim == 0:
                GLOBFRASE += 1
                funvars.append((t[-2], 0, GLOBFRASE, dim, dim1, dim2))
            elif dim == 1:
                for x in range(dim1+1):
                    GLOBFRASE += 1
                    funvars.append((t[-2], 0, GLOBFRASE, dim, dim1, dim2))
                dim1 = None
            elif dim == 2:
                for x in range(dim1+1):
                    for y in range(dim2+1):
                        GLOBFRASE += 1
                        funvars.append((t[-2], 0, GLOBFRASE, dim, dim1, dim2))
                dim1 = None
                dim2 = None
    else:
        if tipoactual == 1:
            if dim == 0:
                LOCALENTERO += 1
                funvars.append((t[-2], 0, LOCALENTERO, dim, dim1, dim2))
            elif dim == 1:
                for x in range(dim1+1):
                    LOCALENTERO += 1
                    funvars.append((t[-2], 0, LOCALENTERO, dim, dim1, dim2))
                dim1 = None
            elif dim == 2:
                for x in range(dim1+1):
                    for y in range(dim2+1):
                        LOCALENTERO += 1
                        funvars.append((t[-2], 0, LOCALENTERO, dim, dim1, dim2))
                dim1 = None
                dim2 = None
        elif tipoactual == 2:
            if dim == 0:
                LOCALDECIMAL += 1
                funvars.append((t[-2], 0, LOCALDECIMAL, dim, dim1, dim2))
            elif dim == 1:
                for x in range(dim1+1):
                    LOCALDECIMAL += 1
                    funvars.append((t[-2], 0, LOCALDECIMAL, dim, dim1, dim2))
                dim1 = None
            elif dim == 2:
                for x in range(dim1+1):
                    for y in range(dim2+1):
                        LOCALDECIMAL += 1
                        funvars.append((t[-2], 0, LOCALDECIMAL, dim, dim1, dim2))
                dim1 = None
                dim2 = None
        elif tipoactual == 3:
            if dim == 0:
                LOCALESVERDAD += 1
                funvars.append((t[-2], 0, LOCALESVERDAD, dim, dim1, dim2))
            elif dim == 1:
                for x in range(dim1+1):
                    LOCALESVERDAD += 1
                    funvars.append((t[-2], 0, LOCALESVERDAD, dim, dim1, dim2))
                dim1 = None
            elif dim == 2:
                for x in range(dim1+1):
                    for y in range(dim2+1):
                        LOCALESVERDAD += 1
                        funvars.append((t[-2], 0, LOCALESVERDAD, dim, dim1, dim2))
                dim1 = None
                dim2 = None
        elif tipoactual == 4:
            if dim == 0:
                LOCALFRASE += 1
                funvars.append((t[-2], 0, LOCALFRASE, dim, dim1, dim2))
            elif dim == 1:
                for x in range(dim1+1):
                    LOCALFRASE += 1
                    funvars.append((t[-2], 0, LOCALFRASE, dim, dim1, dim2))
                dim1 = None
            elif dim == 2:
                for x in range(dim1+1):
                    for y in range(dim2+1):
                        LOCALFRASE += 1
                        funvars.append((t[-2], 0, LOCALFRASE, dim, dim1, dim2))
                dim1 = None
                dim2 = None
    dim = 0


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
	global tipoactual
	if t[1] == 'entero':
		tipoactual = 1
		#if func == 0:
		#	GLOBENTERO += GLOBENTERO 
			#direccion = GLOBENTERO
		#else:
		#	LOCALENTERO +=1
		#	direccion = LOCALENTERO
	elif t[1] == 'decimal':
		tipoactual = 2
		if func == 0:
			GLOBDECIMAL +=1
			direccion = GLOBDECIMAL
		else:
			LOCALDECIMAL +=1
			direccion = LOCALDECIMAL
	elif t[1] == 'esVerdad':
		tipoactual = 3
		if func == 0:
			GLOBESVERDAD +=1
			direccion = GLOBESVERDAD
		else:
			LOCALESVERDAD +=1
			direccion = LOCALESVERDAD
	elif t[1] == 'frase':
		tipoactual = 4
		if func == 0:
			GLOBFRASE +=1
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
    'funcion : FUNCION funcion_increase_func tipo ID funcion_push_id LPAREN funparam RPAREN LLLAVE vars bloque return RLLAVE'
    global funnombre
    global funtipo
    global funcuad
    global funparam
    global funvars
    directorio.append(list((funnombre, funtipo, cuadproc() - 1, funparam, funvars, dirfuncion)))

def p_return(t):
    'return : REGRESA expresion'
    global dirfuncion
    pila_id(dirfuncion)
    ret()
    
    
def p_funcion_increase_func(t):
    'funcion_increase_func : '
    global func
    global funcuad
    func += 1

def p_funcion_push_id(t):
    'funcion_push_id : '
    global GLOBENTERO, GLOBDECIMAL, GLOBESVERDAD, GLOBFRASE
    global funnombre
    global funtipo
    global tipoactual
    global dirfuncion
    funtipo = tipoactual
    funnombre = t[-1]
    if tipoactual == 1:
        GLOBENTERO += 1
        dirfuncion = GLOBENTERO
        
    elif tipoactual == 2:
        GLOBDECIMAL += 1
        dirfuncion = GLOBDECIMAL
        
    elif tipoactual == 3:
        GLOBESVERDAD += 1
        dirfuncion = GLOBESVERDAD
        
    elif tipoactual == 4:
        GLOBFRASE += 1
        dirfuncion = GLOBFRASE
       
        
    
    #creamos espacio en memoria para la funcion
    

def p_funparam(t):
    '''funparam : tipo ID funparam_push_id funparams
                | empty'''
                
def p_funparam_push_id(t):
    'funparam_push_id : '
    global LOCALENTERO
    global LOCALDECIMAL
    global LOCALESVERDAD
    global LOCALFRASE
    if tipoactual == 1:
        LOCALENTERO += 1
        funparam.append((t[-1], 0, LOCALENTERO))
    elif tipoactual == 2:
        LOCALDECIMAL += 1
        funparam.append((t[-1], 0, LOCALDECIMAL))
    elif tipoactual == 3:
        LOCALESVERDAD += 1
        funparam.append((t[-1], 0, LOCALESVERDAD))
    elif tipoactual == 4:
        LOCALFRASE += 1
        funparam.append((t[-1], 0, LOCALFRASE))


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
    'asignacion : ID call_or_array asignacion_push_id IGUAL asignacion_push_igual expresion SEMICOL'
    print("asignacion")
    assign()
    
def p_asignacion_push_id(t):
    'asignacion_push_id :'
    for x in directorio[0][4]:
        if x[0] == t[-2]:
            if x[3] == 0:
                pila_id(list(x)[2])
                break
            elif x[3] == 1:
                pila_id(list(x)[2]+llamadim1+1)
                break
            elif x[3] == 2:
                pila_id(list(x)[2]+llamadim1*(list(x)[5]+1)+llamadim2)
                break
        else:
            for x in directorio[func][4]:
                if x[0] == t[-2]:
                    if x[3] == 0:
                        pila_id(list(x)[2])
                        break
                    elif x[3] == 1:
                        pila_id(list(x)[2]+llamadim1+1)
                        break
                    elif x[3] == 2:
                        pila_id(list(x)[2]+llamadim1*(list(x)[5]+1)+llamadim2)
                        break
                else:
                	for x in directorio[func][3]:
                		if x[0] == t[-2]:
                			pila_id(list(x)[2])
                
            
def p_asignacion_push_igual(t):
    'asignacion_push_igual :'
    pila_op(8)

def p_llamada(t):
	'llamada : ID LPAREN llamadaparam RPAREN'

def p_llamadaparam(t):
	'''llamadaparam : expresion llamadaparams
					| empty'''

def p_llamadaparams(t):
	'''llamadaparams : COMMA llamadaparam
					 | empty'''
		
	

def p_expresion(t):
    '''expresion : exp expresions
                 | LEE LPAREN STRING RPAREN SEMICOL'''
    print("expresion", t[1])
    
        
def p_expresions(t):
    '''expresions : MAYOR expresions_push_mayor exp
                  | MENOR expresions_push_menor exp 
                  | COMPARA expresions_push_compara exp
                  | exp
                  | empty'''
    relacional()
                  
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
    expresion() 

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
    termino()
    
    
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
    '''valor : ID call_or_array
             | CTEINT
             | CTEDEC'''
    global CONSTENTERO
    global CONTSTDECILMAL
    global CONSTDECIMAL
    global CONSTESVERDAD
    global CONSTFRASE
    global GLOBENTERO
    global LOCALENTERO
    global GLOBDECIMAL
    global LOCALDECIMAL
    global GLOBESVERDAD
    global LOCALESVERDAD
    global GLOBFRASE
    global LOCALFRASE
    global directorio
    global directorioconst
    global llamadim1
    global llamadim2
    global dirvalor
    if isinstance(t[1], int):
            directorioconst[t[1]] = CONSTENTERO
            dirvalor = CONSTENTERO
            pila_id(CONSTENTERO)
            CONSTENTERO +=1
    elif isinstance(t[1], float):
            directorioconst[t[1]] = CONSTDECIMAL
            dirvalor = CONSTDECIMAL
            pila_id(CONSTDECIMAL)
            CONSTDECIMAL +=1
    elif isinstance(t[1], str):
        for x in directorio[0][4]:
            if x[0] == t[1]:
            	if x[3] == 0:
                    pila_id(list(x)[2])
                    dirvalor = list(x)[2]
                    break
                elif x[3] == 1:
                    pila_id(list(x)[2]+llamadim1+1)
                    dirvalor = list(x)[2]+llamadim1+1
                    break
                elif x[3] == 2:
                    print (llamadim1,(list(x)[5]+1), llamadim2  )
                    pila_id(list(x)[2]+llamadim1*(list(x)[5]+1)+(llamadim2))
                    dirvalor = list(x)[2]+llamadim1*(list(x)[5]+1)+(llamadim2)
                    break
            else:
                for x in directorio[func][4]:
                    if x[0] == t[1]:
                        if x[3] == 0:
                            pila_id(list(x)[2])
                            dirvalor = list(x)[2]
                            break
                        elif x[3] == 1:
                            pila_id(list(x)[2]+llamadim1+1)
                            dirvalor = list(x)[2]+llamadim1+1
                            break
                        elif x[3] == 2:
                        	pila_id(list(x)[2]+llamadim1*(list(x)[5]+1)+llamadim2)
                        	dirvalor = list(x)[2]+llamadim1*(list(x)[5]+1)+llamadim2
                        	break
                    else:
                    	for x in directorio[func][3]:
                    		if x[0] == t[1]:
                    			pila_id(list(x)[2])
                    			dirvalor = list(x)[2]
                    			break
                    		else:
                    			for x in directorio:
                    				if x[0] == t[1]:
                    					pila_id(directorio[list(x)][5])
                    					dirvalor = directorio[list(x)[5]]
        
def p_call_or_array(t):
    '''call_or_array : LBRAK CTEINT push_array_dim1 RBRAK id_array
                     | LPAREN nombre_func expresion set_value_param id_call RPAREN push_gosub
                     | empty'''

        
def p_nombre_func(t):
    'nombre_func : '
    global nombrefunc
    print t[-2]
    nombrefunc = t[-2]

                     
def p_push_gosub(t):
    'push_gosub : '
    global nombrefunc
    global directorio
    for x in directorio:
        print (x[0])
        print (nombrefunc)
        if x[0] == nombrefunc:
            gosub(directorio[directorio.index(x)][2])
            pila_id(directorio[directorio.index(x)][5])
    
def p_set_value_param(t):
    'set_value_param : '
    global directorio
    global paramactual
    global dirvalor
    for x in directorio:
        if x[0] == nombrefunc:
            param(dirvalor, directorio[directorio.index(x)][3][paramactual][2])
            paramactual += 1

def p_id_array(t):
	'''id_array : LBRAK CTEINT push_array_dim2 RBRAK
				| empty'''
				
def p_push_array_dim1(t):
	'push_array_dim1 : '
	global llamadim1
	llamadim1 = t[-1]

def p_push_array_dim2(t):
	'push_array_dim2 : '
	global llamadim2
	llamadim2 = t[-1]

def p_id_call(t):
	'''id_call : COMMA expresion set_value_param id_call
			   | empty'''
	

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