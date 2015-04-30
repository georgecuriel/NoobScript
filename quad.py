
cont=1
contemp=0
cuadruplos = [[0 for x in range(5)] for x in range(300)] 
cuadro = 2
i=0
j=0

#Crear las pilas e inicializarlas
#pila de operadores
PilaO = [] #pila de operandos
PSaltos = [] #pila de saltos
POper = [] #pila de operadores

def init(): 

  # PilaO=createStack(100); #pila de operandos
  # PSaltos=createStack(100); #pila de saltos
  # POper=createStack(100); #pila de operadores
  cuadf = open(Maquina/cuadruplos.txt, 'w')
  if cuadf == NULL:
    print(stderr, "Archivo cuadruplos.txt no se ha podido abrir");
    sys.exit(1);
   
def printcuadruplos():
    for i in range(300):
        for j in range(5):
          if cuadruplos[i][j]== 0:
              exit(1)
        print( repr(cuadf), repr(cuadruplos[i][j]))
    print(repr(cuadf)) ;
  

#impresion de de direccion en memoria y de valor asignado de la variable dependiendo de su tipo  
def escribe_ctei(dire, val):
  print(repr(cuadf),"-1", repr(dire), repr(val))

def escribe_ctef(dire, val):
  print(repr(cuadf),"-1", repr(dire), repr(val))

def escribe_ctes(dire, val):
  print(repr(cuadf),"-1", repr(dire), repr(val))
  
  
def escribe_cuad(cuadro, ope, oper1, oper2, res):
    print("Imprimiendo:", repr(cuadro),repr(ope), repr(oper1), repr(oper2), repr(res))
    cuadruplos[cuadro-1][0] = cuadro
    cuadruplos[cuadro-1][1] = ope
    cuadruplos[cuadro-1][2] = oper1
    cuadruplos[cuadro-1][3] = oper2
    cuadruplos[cuadro-1][4] = res
    cont = cont+1;
   

#1
def pila_id(oper):
    PilaO.append(oper)
    print(stderr, "Ya meti oper \n", repr(oper))
   
#2
def pila_op(op):
    POper.append(op)
    print(stderr, "ya meti op \n", repr(op))
   
#3
def parentesisPush():
    POper.append(11)  #genera pared falsa en pila
   
def parentesisPop():
    POper.pop #saca de la pila  
      
#5
def termino(): 
  print(stderr, "Estoy en cuadruplo termino\n")
  op = POper[-1]
  POper.pop
  if op == 3 or op == 4:      #operadores * o /
    oper2 = PilaO[-1]
    PilaO.pop
    oper1 = PilaO[-1]
    PilaO.pop
    if (check(op, oper1, oper2)):   #checa si es valido
      escribe_cuad(cont, op, oper1, oper2, contemp+tipotemp())  #genera el cuadruplo
      pila_id(contemp+tipotemp())     #mete el resultado a la pila de operadores
      contemp = contemp+1
    
    else: #marca error si no es compatible
      print(stderr, "***ERROR DE TIPOS**** termino\n")
      exit(1)
  else:
      fprintf(stderr, "No es termino pasar al siguiente \n")
      pila_op(op)
   
#6
def expresion():
  print(stderr, "Estoy en cuadruplo expresion\n")
  op = PilaO[-1]
  POper.pop
  if op == 1 or op == 2:        #operadores + o -
    oper2 = PilaO[-1]
    PilaO.pop
    oper1 = PilaO[-1]
    pop(PilaO);
    if check(op, oper1, oper2):   #checa el tipo    
      escribe_cuad(cont, op, oper1, oper2,  (contemp+tipotemp())) #genera el cuadruplo
      pila_id(contemp+tipotemp())     #mete el resultado a la pila de operadores
      contemp = contemp+1
    else:   #marca error si no es compatible
      print(stderr, "***ERROR DE TIPOS**** expresion\n")
      exit(1)
  else:
    print(stderr, "No es expresion pasar al siguiente \n")
    pila_op(op)
     
#7
def relacional():
    print(stderr, "Estoy en cuadruplo relacional\n");
    op = POper[-1]
    POper.pop
    if op == 5 or op == 6 or op == 7 :  # op == < || op == > || op = ==
        oper2 = PilaO[-1] 
        PilaO.pop
        oper1 = PilaO[-1]
        PilaO.pop
        if check(op, oper1, oper2):   #checa el tipo
          escribe_cuad(cont, op, oper1, oper2,  (contemp+tipotemp()))
          pila_id(contemp+tipotemp());      #mete el resultado a la pila de operadores
          contemp = contemp + 1;
         
        else:   #marca error si no es compatible
          print(stderr, "***ERROR DE TIPOS**** relacional\n");
          exit(1);

    else:
        print(stderr, "No es relacional pasar al siguiente \n");
        pila_op(op);

#8
def assign():
  print(stderr, "Estoy en quad assign\n")
  op = POper[-1] 
  POper.pop
  if op == 10:  #si el operador es =
    oper2 = PilaO[-1] 
    PilaO.pop 
    oper1 = PilaO[-1]
    PilaO.pop
    if check(op, oper1, oper2): #checa el tipo
      escribe_cuad(cont, op,  oper2, -1, oper1)   #genera el cuadruplo
      contemp = contemp + 1 
    
    else:   #marca error si no es compatible
      print(stderr, "***ERROR DE TIPOS**** assign\n")
      exit(1)
         
  else:
    print(stderr, "No es asignacion pasar al siguiente \n")
    pila_op(op)
    
  #15
def logico():
    print(stderr, "Estoy en cuad logico\n");
    op = top(POper)
    pop(POper)
    if op == 8 or op == 9: # op == & || op == |
      oper2 = top(PilaO)
      pop(PilaO)
      oper1 = top(PilaO)
      pop(PilaO)
      if check(op, oper1, oper2):   #checa el tipo
        escribe_cuad(cont, op, oper1, oper2,  (contemp+tipotemp()))
        pila_id(contemp+tipotemp())   # mete el resultado a la pila de operadores
        contemp = contemp + 1
    
      else:   #marca error si no es compatible
        print(stderr, "***ERROR DE TIPOS**** logico\n")
        exit(1)
         
    else:
      fprintf(stderr, "No es logico, pasar al siguiente \n")
      pila_op(op)
      
#10
def if1():
  print(stderr, "Estoy en cuadruplo if\n")
  #if
  #1.- genera gotoF y mete cont-1 a la pila de saltos
  op = 20
  oper1 = PilaO[-1]
  if per1 < 10000 or oper1>=11000:
    print (stderr, "***ERROR DE TIPOS**** IF\n")
  else:
    POper.pop
    escribe_cuad(cont, op, oper1, -1, -1)
    PSaltos.append(cont-1)
    
#11
def else1():
#2genera goto (else), y saca falso de la pila y rellena el primer salto
  op = 22 #goto
  escribe_cuad(cont, op, -1, -1, -1);
  falso = PSaltos[-1]
  cuadruplos[falso-1][4]=cont
  PSaltos.append(cont-1)
#12
def if2():
  fin = PSaltos[-1]
  PSaltos.pop
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
  
def print1():
  op=33
  POper.append(op)

def print2():
  oper1=top(PilaO)
  escribe_cuad(cont,top(POper),oper1,-1,-1)

def cuadproc():
  return cont




  
