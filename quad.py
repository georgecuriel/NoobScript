from cubo import check, tipotemp

cont=1
contemp=0
cuadruplos = [[0 for x in range(5)] for x in range(300)] 

#Crear las pilas e inicializarlas
#pila de operadores
PilaO = [] #pila de operandos
PSaltos = [] #pila de saltos
POper = [] #pila de operadores
cuadf = None

def init(): 

  # PilaO=createStack(100); #pila de operandos
  # PSaltos=createStack(100); #pila de saltos
  # POper=createStack(100); #pila de operadores
  global cuadf
  cuadf = open("cuadruplos.txt", 'w')
  if cuadf == None:
    print( "Archivo cuadruplos.txt no se ha podido abrir");
   
def printcuadruplos():
  for i in range(300):
    for j in range(5):
      if cuadruplos[i][j]== 0:
        exit(1)
      global cuadf
      cuadf.write(repr(cuadruplos[i][j]) + " ")
    cuadf.write("\n") ;
  

#impresion de de direccion en memoria y de valor asignado de la variable dependiendo de su tipo  
def escribe_ctei(dire, val):
  cuadf.write("%d %d %d\n",s,dire,val)

def escribe_ctef(dire, val):
  cuadf.write("%d %d %d\n",s,dire,val)

def escribe_ctes(dire, val):
  cuadf.write("%d %d %d\n",s,dire,val)

def escribe_cuad(cuadro, ope, oper1, oper2, res):
    print("Imprimiendo:", repr(cuadro),repr(ope), repr(oper1), repr(oper2), repr(res))
    cuadruplos[cuadro-1][0] = cuadro
    cuadruplos[cuadro-1][1] = ope
    cuadruplos[cuadro-1][2] = oper1
    cuadruplos[cuadro-1][3] = oper2
    cuadruplos[cuadro-1][4] = res
    global cont
    cont = cont + 1
   

#1
def pila_id(oper):
    PilaO.append(oper)
    print( "Ya meti oper \n", repr(oper))
   
#2
def pila_op(op):
    POper.append(op)
    print( "ya meti op \n", repr(op))
   
#3
def parentesisPush():
    POper.append(9)  #genera pared falsa en pila
   
def parentesisPop():
    POper.pop #saca de la pila  
      
#5 ARREGLAR
def termino():
  global contemp
  print( "Estoy en cuadruplo termino (el de multiplicaciones)\n")
  op = POper[-1]
  POper.pop()
  if op == 3 or op == 4:      #operadores * o /
    oper2 = PilaO[-1]
    PilaO.pop()
    oper1 = PilaO[-1]
    PilaO.pop()
    if (check(op, oper1, oper2)):   #checa si es valido
      escribe_cuad(cont, op, oper1, oper2, contemp+tipotemp())  #genera el cuadruplo
      pila_id(contemp+tipotemp())     #mete el resultado a la pila de operadores
      contemp = contemp+1
    
    else: #marca error si no es compatible
      print( "***ERROR DE TIPOS**** termino\n")
      exit(1)
  else:
      print( "No es termino pasar al siguiente \n")
      pila_op(op)
   
#6
def expresion():
  global contemp
  print( "Estoy en cuadruplo expresion (suma y resta)")
  op = POper[-1]
  POper.pop()
  if op == 1 or op == 2:        #operadores + o -
    oper2 = PilaO[-1]
    PilaO.pop()
    oper1 = PilaO[-1]
    PilaO.pop()
    if check(op, oper1, oper2):   #checa el tipo    
      escribe_cuad(cont, op, oper1, oper2,  contemp+tipotemp()) #genera el cuadruplo
      pila_id(contemp+tipotemp())     #mete el resultado a la pila de operadores
      contemp = contemp+1
    else:   #marca error si no es compatible
      print( "***ERROR DE TIPOS**** expresion\n")
      exit(1)
  else:
    print( "No es expresion pasar al siguiente \n")
    pila_op(op)
     
#7
def relacional():
    print( "Estoy en cuadruplo relacional\n ");
    global contemp
    op = POper[-1]
    POper.pop()
    if op == 5 or op == 6 or op == 7 :  # op == < || op == > || op = ==
        oper2 = PilaO[-1] 
        PilaO.pop()
        oper1 = PilaO[-1]
        PilaO.pop()
        if check(op, oper1, oper2):   #checa el tipo
          escribe_cuad(cont, op, oper1, oper2, contemp+tipotemp())
          pila_id(contemp+tipotemp());     #mete el resultado a la pila de operadores
          contemp = contemp + 1 
         
        else:   #marca error si no es compatible
          print( "***ERROR DE TIPOS**** relacional\n");
          exit(1)

    else:
        print( "No es relacional pasar al siguiente \n");
        pila_op(op)

#8

def assign():
  global contemp
  print("Estoy en quad assign\n")
  op = POper[-1] 
  POper.pop()
  if op == 8:  #si el operador es =
    oper2 = PilaO[-1]
    PilaO.pop() 
    oper1 = PilaO[-1]
    PilaO.pop()
    if check(op, oper1, oper2): #checa el tipo
      escribe_cuad(cont, op,  oper2, -1, oper1)   #genera el cuadruplo
      contemp = contemp + 1
      
    else:   #marca error si no es compatible
      print( "Error de tipos en assign\n")
      exit(1)
         
  else:
    print( "No es asignacion pasar al siguiente \n")
    pila_op(op)
      
#10
def if1():
  global cont
  print( "Estoy en cuadruplo if\n")
  #if
  #1.- genera gotoF y mete cont-1 a la pila de saltos
  op = 20
  oper1 = PilaO[-1]
  if oper1 <= 2000 and oper1 > 2500 or oper1 <= 4000 and oper1 > 4500 or oper1 <= 6000 and oper1 > 6500 or oper1 <= 8000 and oper1 > 8500:
    print ("***ERROR DE TIPOS**** IF\n") #STANDAR ERROR DE PYTHON CHECAR
  else:
    POper.pop()
    escribe_cuad(cont, op, oper1, -1, -1)
    PSaltos.append(cont-1)
    
#11
def else1():
  global cont
#2genera goto (else), y saca falso de la pila y rellena el primer salto
  op = 22 #goto
  escribe_cuad(cont, op, -1, -1, -1)
  falso = PSaltos[-1]
  cuadruplos[falso-1][4]=cont
  PSaltos.append(cont-1)

def ret():
  valor = PilaO.pop()
  direccion =  PilaO.pop()
  escribe_cuad(cont, 34, valor,-1, direccion)

  
  

def if2():
  fin = PSaltos[-1]
  PSaltos.pop()
  cuadruplos[fin-1][4]=cont
  #13
  
def do1():
  #do-while
  #1.- mete cont a pila de saltos
  PSaltos.append(cont)
  #14
def do2(): 
  #2.- genra gotoV e incrementa el cont
  op = 21 #gotov
  oper1 = Pila0[-1]
  oper2 = -1
  escribe_cuad(cont, op, oper1, -1, contemp)


def gosub(quadInicio):
  escribe_cuad(cont, 32, quadInicio, -1, -1)
  

def param(valor, param):
  escribe_cuad(cont, 31,valor ,-1,param)

def print1():
  op=33
  POper.append(op)

def print2():
  oper1=PilaO[-1]
  escribe_cuad(cont,POper[-1],oper1,-1,-1)
  
def cuadproc():
  return cont

