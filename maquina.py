from local import *
from temporal import *
from constant import *
from globales import *

auxCont = 0

def checaScope(dire):
    if dire >= 1000 and dire < 2500:    #Direcciones de variables globales
        return 1
    elif dire >= 3000 and dire < 4500:  #Direcciones de variables locales
        return 2        
    elif dire >= 5000 and dire < 6500:  #Direcciones de variables temporales
        return 3
    else:
        return 4        #Regresa 4 si no es de ninguna de las otras memorias
#Metodo que determina el tipo de la variable que se usara. Si entra en alguno de los rangos especificados se regresa el tipo
#double o boolean (dependiendo del caso), sino se regresa el tipo int 
def checaTipo(dire):
    if  dire == -1:
        return -1   #//Si no hay una direccion en alguno de los elementos del cuadruplo
    #rangos de variables float en las memorias
    elif dire >= 1500 and dire < 2000 or dire >= 3500 and dire < 4000 or dire >= 5500 and dire < 6000 or dire >= 7500 and dire < 8000:
        return 2
    #Rangos de variables boolean en las memorias
    elif dire >= 2000 and dire < 2500 or dire >= 4000 and dire < 4500 or dire >= 6000 and dire < 6500 or dire >= 8000 and dire < 8500:
        return 3
    #Rangos de variables string en las memorias  
    elif dire >= 2500 and dire < 3000 or dire >= 4500 and dire < 5000 or dire >= 6500 and dire < 7000 or dire >= 8500 and dire < 9000:
        return 4
    #si no pues es entero
    else:
        return 1

def obtenValorD(scope,dire, tipo):
    if scope == 1:
        return memglobal.getValD(dire, tipo)
    elif scope == 2:
        return memlocal.getValD(dire, tipo)
    elif scope ==3:
        return memtemp.getValD(dire, tipo)
    else: #case  4:
        return memconstant.getValD(dire, tipo)

def meteValorD(scope, dire, val, tipo):
    
    if scope == 1:
        memglobal.setValD(dire, val, tipo)
    elif scope == 2:  
        memlocal.setValD(dire, val, tipo)
    elif scope == 3:
        memtemp.setValD(dire, val, tipo)
    else:
        memconstant.setValD(dire, val, tipo)

def obtenValorS( scope, dire):
    def uno():  #    case 1:
        return memglobal.getMemString(dire)
    def dos(): #case 2:
        return memlocal.getMemString(dire)
    def tres():      # case 3:
        return memtemp.getMemString(dire)
    def cuatro(): #case 4 :
        return memconstant.getMemString(dire)
    operaciones = { 1: uno, 2: dos, 3: tres, 4: cuatro} 
    operaciones[scope]()

def meteValorS(scope, val, dire):
    def uno():
        memglobal.setMemString(dire, val)
    def dos():           
        memlocal.setMemString(dire, val)
    def tres():
        memtemp.setMemString(dire, val)
    def cuatro():
        emconstant.setMemString(dire, val)
    operaciones = { 1: uno, 2: dos, 3: tres, 4: cuatro} 
    operaciones[scope]()

def obtenValorB(scope, dire):
    if scope == 1:
        return memglobal.getMemBool(dire)
    if scope == 2:
        return memlocal.getMemBool(dire)
    if scope == 3:
        return memtemp.getMemBool(dire)

    
def meteValorB(scope, dire, val):
    def uno() : #case 1:
        memglobal.setMemBool(dire, val)
    def dos():    
        memlocal.setMemBool(dire, val)
    def tres():
        memtemp.setMemBool(dire, val)
    operaciones = { 1: uno, 2: dos, 3: tres}
    operaciones[scope]()
    
#Inicializas Espacios en memoria con la clase correspondiente
memglobal = Global()
memlocal = Local()
memconstant = Constant()
memtemp = Temporal()
x_table = []
cuad = [[]]
cont1 = 0
cont2 = 0

for x in memconstant.constantes:
    opcion = checaTipo(memconstant.constantes[memconstant.constantes.index(x)][1])
    print memconstant.constantes[memconstant.constantes.index(x)]

    if opcion == 1 or opcion == 2:
        memconstant.setValD(memconstant.constantes[memconstant.constantes.index(x)][1], memconstant.constantes[memconstant.constantes.index(x)][0], opcion)
        print (memconstant.constantes[memconstant.constantes.index(x)][1], memconstant.constantes[memconstant.constantes.index(x)][0], opcion)
    else:
        memconstant.setMemString(memconstant.constantes[memconstant.constantes.index(x)][1], memconstant.constantes[memconstant.constantes.index(x)][0], opcion)

for eachLine in open('cuadruplos.txt', "r"):
    cuad.append([int(k) for k in eachLine.split()])
    cont2 = cont2 + 1
    #El operador es el segundo elemento del arreglo obtenido
cuad.append([cont2+1, 666,-1,-1,-1])
op=0


while op is not 666:
    
    cont1 = cont1 + 1
    print ("estoy en la linea", cont1) 
    op =  cuad[cont1][1]
    scope = checaScope(cuad[cont1][2])
    scope2 = checaScope(cuad[cont1][3])
    scope3 = checaScope(cuad[cont1][4])
    #Revisar el tipo de cada operando
    tipo1 = checaTipo(cuad[cont1][2])
    tipo2 = checaTipo(cuad[cont1][3])
    tipo3 = checaTipo(cuad[cont1][4])

    
    def suma(op):  # case 1 +
        global scope
        global scope2
        global scope3
        global tipo1
        global tipo2
        global tipo3
        global cuad
        ope1 = obtenValorD(scope, cuad[cont1][2], tipo1)
        print ope1
        ope2 = obtenValorD(scope2, cuad[cont1][3], tipo2)
        print ope2
        meteValorD(scope3, cuad[cont1][4], (ope1 + ope2), tipo3)
    def resta(op): # case 2: -
        global scope
        global scope2
        global scope3
        global tipo1
        global tipo2
        global tipo3
        global cuad
        ope1 = obtenValorD(scope, cuad[cont1][2], tipo1)
        ope2 = obtenValorD(scope2, cuad[cont1][3], tipo2)
        meteValorD(scope3, cuad[cont1][4], (ope1 - ope2), tipo3)
    def multiplicacion(op): #case 3: *
        global scope
        global scope2
        global scope3
        global tipo1
        global tipo2
        global tipo3
        global cuad
        ope1 = obtenValorD(scope, cuad[cont1][2], tipo1)
        print ope1
        ope2 = obtenValorD(scope2, cuad[cont1][3], tipo2)
        print ope2
        meteValorD(scope3, cuad[cont1][4], (ope1 * ope2), tipo3)
    def division(op): #case 4: /
        global scope
        global scope2
        global scope3
        global tipo1
        global tipo2
        global tipo3
        global cuad
        ope1 = obtenValorD(scope, cuad[cont1][2], tipo1)
        ope2 = obtenValorD(scope2, cuad[cont1][3], tipo2)
        meteValorD(scope3, cuad[cont1][4], (ope1 / ope2), tipo3)
    def menor(op): #case 5: <
        global scope
        global scope2
        global scope3
        global tipo1
        global tipo2
        global tipo3
        global cuad
        ope1 = obtenValorD(scope, cuad[cont1][2], tipo1)
        ope2 = obtenValorD(scope2, cuad[cont1][3], tipo2)
        meteValorB(scope3, cuad[cont1][4], (ope1 < ope2))
    def mayor(op): #case 6: >
        global scope
        global scope2
        global scope3
        global tipo1
        global tipo2
        global tipo3
        global cuad
        ope1 = obtenValorD(scope, cuad[cont1][2], tipo1)
        ope2 = obtenValorD(scope2, cuad[cont1][3], tipo2)
        meteValorB(scope3, cuad[cont1][4], (ope1 > ope2))
    def comparacion(op): #case 7: ==
        global scope
        global scope2
        global scope3
        global tipo1
        global tipo2
        global tipo3
        global cuad
        ope1 = obtenValorD(scope, cuad[cont1][2], tipo1)
        ope2 = obtenValorD(scope2, cuad[cont1][3], tipo2)
        meteValorB(scope3, cuad[cont1][4], (ope1 == ope2))
    def igualacion(op): #igucalacion case 8 =
        global scope
        global scope2
        global scope3
        global tipo1
        global tipo2
        global tipo3
        global cuad
        def uno(tipo3):
            ope1 = obtenValorD(scope, cuad[cont1][2], tipo1)
            meteValorD(scope3, cuad[cont1][4], ope1, tipo3) #cabiar ope 1
        def dos(tipo3): 
            ope1 = obtenValorD(scope, cuad[cont1][2], tipo1)
            meteValorD(scope3, cuad[cont1][4], ope1, tipo3)
        def tres(tipo3): 
            ope1 = obtenValorB(scope, cuad[cont1][2], tipo1)
            meteValorB(scope3, cuad[cont1][4], opeb)
        def cuatro(tipo3): 
            opes = obtenValorS(scope, cuad[cont1][2], tipo1)
            meteValorS(scope3, cuad[cont1][4], opes)
        operaciones = { 1: uno, 2: dos, 3: tres, 4: cuatro} 
        operaciones[tipo3](tipo3)   
    
    def GOTOF(op):  #case 20: //GOTOF
        global cont1
        global scope
        global scope2
        global scope3
        global tipo1
        global tipo2
        global tipo3
        global cuad
        if obtenValorB(scope,cuad[cont1][2]) == 1:
            print ("siguele ")
        else:
            cont1 = cuad[cont1][4]
    def GOTOV(op): #case 21: //GOTOV
        if obtenValorB(scope,cuad[cont1][2]) == 0:
            print ("siguele ")
        else:
            cont1 = cuad[cont1][4]
    def GOTO(op): #case 22: //GOTO
        global cont1
        global scope
        global scope2
        global scope3
        global tipo1
        global tipo2
        global tipo3
        global cuad
        cont1 = cuad[cont1][4] -1
        
        
        
    def PARAM(op): #case 31: //PARAM
        if tipo1 == 1 or tipo1 == 2:
            val = obtenValorD(scope, cuad[cont1][2], tipo1)
            meteValorD(scope, cuad[cont1][4], val , tipo3)
        elif tipo1== 3:
            val = obtenValorB(scope, cuad[cont1][2], tipo1)
            meteValorB(scope, cuad[cont1][4], val , tipo3)
        else:
            val = obtenValorS(scope, cuad[cont1][2], tipo1)
            meteValorS(scope, cuad[cont1][4], val , tipo3)
    
    def GOsub(op): #case 32: //Gosub
        global auxCont
        global cont1
        auxCont = cont1
        print auxCont
        cont1 = cuad[cont1][2] - 1
        print cont1
        
    def ret(op): #Case 34 return
        global auxCont
        global scope
        global scope2
        global scope3
        global tipo1
        global tipo2
        global tipo3
        global cuad
        global cont1
        if tipo1 == 1 or tipo1 == 2:
            val = obtenValorD(scope, cuad[cont1][2], tipo1)
            meteValorD(scope3, cuad[cont1][4], val , tipo3)
        elif tipo1== 3:
            val = obtenValorB(scope, cuad[cont1][2], tipo1)
            meteValorB(scope3, cuad[cont1][4], val , tipo3)
        else:
            val = obtenValorS(scope, cuad[cont1][2], tipo1)
            meteValorS(scope3, cuad[cont1][4], val , tipo3)     
        if auxCont == 0:
            print("No ha sido llamada la funcion")
        else:
            cont1 = auxCont
            print cont1
    

    def write(op): #case 33: //Write
        global scope
        global scope2
        global scope3
        global tipo1
        global tipo2
        global tipo3
        global cuad
        global ope1
        if tipo1 == 1: #case 1:
            if scope == 1:
                ope1 = memglobal.getValD(cuad[cont1][2], tipo1)
            elif scope == 2:
                ope1 = memlocal.getValD(cuad[cont1][2], tipo1)
            elif scope ==3:
                ope1 = memtemp.getValD(cuad[cont1][2], tipo1)
            else:
                ope1 = memconstant.getValD(cuad[cont1][2], tipo1)
            print(ope1)
        elif tipo1 == 2: #case 2:
            if scope == 1:
                ope1 = memglobal.getValD(cuad[cont1][2], tipo1)
            elif scope == 2:
                ope1 = memlocal.getValD(cuad[cont1][2], tipo1)
            elif scope ==3:
                ope1 = memtemp.getValD(cuad[cont1][2], tipo1)
            else:
                ope1 = memconstant.getValD(cuad[cont1][2], tipo1)
            print(ope1)
        elif tipo1 == 4:
            if scope == 1:
                ope1 = memglobal.getValString(cuad[cont1][2], tipo1)
            elif scope == 2:
                ope1 = memlocal.getValDString(cuad[cont1][2], tipo1)
            elif scope ==3:
                ope1 = memtemp.getValDString(cuad[cont1][2], tipo1)
            else:
                ope1 = memconstant.getValDString(cuad[cont1][2], tipo1)
            print(ope1)
    def salir(op):
        print "ya acabe"
        exit(1)
    operaciones = { 1: suma, 2: resta, 3: multiplicacion, 4: division, 5: menor, 6:mayor, 7:comparacion, 8:igualacion, 20:GOTOF, 21:GOTOV, 22:GOTO, 31:PARAM, 32: GOsub, 33:write, 34:ret, 666: salir} 
    operaciones[op](op) 
    print("\n")
    
    #--->cerrar archivo
    #todo que devuelve el scope de un operando, recibe la direcci?on de la variables
    #y determina la memoria a la que pertenece por medio de los rangos.
