#Cubo Semantico
tipo = -1

def suma(op, operando1 , operando2): 
    global tipo
    print  ("Estoy en el case suma Operando1:%s Operando2:%s\n" % (operando1, operando2))
    
    if operando1 == 'es' or operando1=='f':
        print ("no se puede")
        return False
        
    elif operando1 == 'e':
        if operando2 == 'e':
            print ("si se puede y es entero")
            tipo = 5000
            return True
        elif operando2 == 'd':
            print ("si se puede y es Decimal")
            tipo = 5500
            return True
        else:
            print ("no se puede nigga")
            return False
            
    elif operando1 == 'd':
        if operando2 == 'e':
            print ("si se puede y es Decimal")
            tipo = 5500
            return True
        
        elif operando2 == 'f':
            print ("si se puede y es Decimal")
            tipo = 5500
            return True
        else:
            print ("no se puede nigga")
            return False
            
    else:
        return False

def resta(op, operando1 , operando2):
    global tipo
    print ("Estoy en el case resta Operando1:%s Operando2:%s\n" % (operando1, operando2))
    
    if operando1 == 'f' or operando1 == 'es':
        print ("Nel Carnal")
        return False
   
    elif operando1=='e':
        if operando2 == 'e':
            print ("si se puede y es Entero")
            tipo = 5000
            return True
        
        elif operando2 =='d':
            valido = True
            tipo = 5500
            print ("si se puede y es Decimal")
            return valido
        else:
            print ("no se puede nigga")
            return False
            
    elif operando1 == 'd':
        if operando2 == 'e':
            print ("si se puede y es Decimal")
            tipo = 5500
            return True
        
        elif operando2 == 'd':
            print ("si se puede y es Decimal")
            tipo = 5500
            return True
        else:
            print ("no se puede nigga")
            return False
    
    else:
        print ("no se puede")
        return False

def multiplicacion(op, operando1 , operando2):
    global tipo
    print ("Estoy en el case multiplicacion Operando1:%s Operando2:%s\n" % (operando1, operando2))
    
    if operando1 == 'es' or operando1 == 'f':
        print ("Nel Carnal")
        return False
        
    elif operando1 == 'e':
        if operando2 =='e':
            print ("si se puede y es Entero")
            tipo = 5000
            return True
            
        elif operando2 == 'd':
            print ("si se puede y es Decimal")
            tipo = 5500
            return True
        else:
            print ("no se puede nigga")
            return False
            
    elif operando1 == 'd':
        if operando2 == 'en':
            print ("si se puede y es Decimal")
            tipo = 5500
            return True
            
        elif operando2 == 'd':
            print ("si se puede y es Decimal")
            tipo = 5500
            return True
        else:
            print ("no se puede nigga")
            return False
    else:
        print ("Nel vatirri")
        return False

def division(op, operando1 , operando2):
    global tipo
    print ("Estoy en el case division!  Operando1:%s Operando2:%s\n" % (operando1, operando2))
    
    if operando1 =='es' or operando1 =='f':
        print ("No se puede")
        return False
        
    elif operando1 =='e':
        if operando2 == 'e':
            print ("si se puede y es Decimal")
            tipo = 5500
            return True
            
        elif operando2 == 'd':
            print ("si se puede y es Decimal")
            tipo = 5500
            return True
        else:
            print ("no se puede nigga")
            return False
            
    elif operando1 == 'd':
        if operando2 == 'e':
            print ("si se puede y es Decimal")
            tipo = 5500
            return True
        
        elif operando2 =='d':
            print ("si se puede y es Decimal")
            tipo = 5500
            return True
        else:
            print ("no se puede nigga")
            return False
    else:
        return False

def menorQue(op, operando1 , operando2):
    print  ("Estoy en el case en menorque <")
    
    if operando1 =='es' or operando1 =='f':
        print ("No se puede")
        return False
    
    if operando1 =='e':
        if operando2 == 'e':
            print ("si se puede y es esVerdad")
            tipo = 6000
            return True
        
        elif operando2 == 'd':
            print ("si se puede y es esVerdad")
            tipo = 6000
            return True
        else:
            print ("no se puede nigga")
            return False
    elif operando1 == 'd':
        if operando2 == 'e':
            print ("si se puede y es esVerdad")
            tipo = 6000
            return True
        
        elif operando2 =='d':
            print ("si se puede y es esVerdad")
            tipo = 6000
            return True
        else:
            print ("no se puede nigga")
            return False
    else:
        return False

def mayorQue(op, operando1 , operando2):
    print ("Estoy en mayor que")
    
    if operando1 =='es' or operando1 =='f':
        print ("Nel Carnal")
        return False
   
    if operando1 =='e':
        if operando2 == 'e':
            print ("si se puede y es esVerdad")
            tipo = 6000
            return True
            
        elif operando2 == 'd':
            print ("si se puede y es esVerdad")
            tipo = 6000
            return True
        else:
            print ("no se puede nigga")
            return False
            
    elif operando1 == 'd':
        if operando2 == 'e':
            print ("si se puede y es esVerdad")
            tipo = 6000
            return True
        elif operando2 =='d':
            print ("si se puede y es esVerdad")
            tipo = 6000
            return True
        else:
            print ("no se puede nigga")
            return False
    else:
        return False         

def igualA(op, operando1 , operando2):
    print  ("Estoy en el case relacional == !  Operando1:%s Operando2:%s\n" % (operando1, operando2))
    
    if operando1 =='f':
        return False
    
    elif operando1 =='e':
        if operando2 == 'e':
            print ("si se puede y es esVerdad")
            tipo = 6000
            return True
            
        elif operando2 == 'd':
            print ("si se puede y es esVerdad")
            tipo = 6000
            return True
            
        elif operando2 == 'es':
            print ("nel carnal")
            return False
        else:
            print ("no se puede nigga")
            return False
            
    elif operando1 == 'd':
        if operando2 == 'e':
            print ("si se puede y es esVerdad")
            tipo = 6000
            return True
            
        elif operando2 =='d':
            print ("si se puede y es esVerdad")
            tipo = 6000
            return True
        else:
            print ("no se puede nigga")
            return False    
    elif operando1 == 'es':
        if operando2 == 'es':
            print ("si se puede y es esVerdad")
            tipo = 6000
            return True
        else:
            print ("no se puede nigga")
            return False
            
    else:
        return False         

def igualacion(op, operando1 , operando2):
    print  ("Estoy en el case de igualacion   Operando1:%s Operando2:%s\n" % (operando1, operando2))
    
    if operando1 =='e':
        if operando2 == 'e':
            print ("si se puede y es entero")
            return True
            
        elif operando2 == 'd':
            print ("si se puede y es decimal")
            return True
        
        else:
            print ("no se puede nigga")
            return False
            
    elif operando1 =='d':
        if operando2 == 'e':
            print ("si se puede y es decimal")
            tipo =  5500
            return True
            
        elif operando2 == 'd':
        	print ("si se puede y es decimal")
        	tipo = 5500
        	return True
        else:
            print ("no se puede nigga")
            return False
            
    elif operando1 =='es':
        if operando2 == 'es':
            print ("booleaaaaaan")
            tipo = 6000
            return True
        else:
            print ("no se puede nigga")
            return False
            
    elif operando1 =='f':
        if operando2 == 'f':
            print ("si se puede y es esFrase")
            tipo = 6500
            return True
        else:
            print ("no se puede nigga")
            return False
    else:
        return False     




def check(op, oper1 , oper2):
    
    #entero
    if oper1 >= 1000 and oper1 < 1500 or oper1 >= 3000 and oper1 < 3500 or oper1 >= 5000 and oper1 < 5500 or oper1 >= 7000 and oper1 < 7500:
        operando1='e'
    
    #decimal
    elif oper1 >= 1500 and oper1 < 2000 or oper1 >= 3500 and oper1 < 4000 or oper1 >= 5500 and oper1 < 6000 or oper1 >= 7500 and oper1 < 8000:
        operando1='d'
    
    #esVerdad
    elif oper1 >= 2000 and oper1 < 2500 or oper1 >= 4000 and oper1 < 4500 or oper1 >= 6000 and oper1 < 6500 or oper1 >= 8000 and oper1 < 8500:
        operando1='es'
    
    #frase
    elif oper1 >= 2500 and oper1 < 3000 or oper1 >= 4500 and oper1 < 5000 or oper1 >= 6500 and oper1 < 7000 or oper1 >= 8500 and oper1 < 9000:
        operando1='f'
    
    #entero
    if oper2 >= 1000 and oper2 < 1500 or oper2 >= 3000 and oper2 < 3500 or oper2 >= 5000 and oper2 < 5500 or oper1 >= 7000 and oper1 < 7500:
        operando2='e'
    
    #decimal
    elif oper2 >= 1500 and oper2 < 2000 or oper2 >= 3500 and oper2 < 4000 or oper2 >= 5500 and oper2 < 6000 or oper1 >= 7500 and oper1 < 8000:
        operando2='d'
    
    #esVerdad
    elif oper2 >= 2000 and oper2 < 2500 or oper2 >= 4000 and oper2 < 4500 or oper2 >= 6000 and oper2 < 6500 or oper1 >= 8000 and oper1 < 8500:
        operando2='es'
    
    #frase
    elif oper2 >= 2500 and oper2 < 3000 or oper2 >= 4500 and oper2 < 5000 or oper2 >= 6500 and oper2 < 7000 or oper1 >= 8500 and oper1 < 9000:
        operando2='f'
    
# Como si fuera switch, pero con arrays associativos
    operaciones = { 1: suma, 2: resta, 3: multiplicacion, 4: division, 5: menorQue, 6: mayorQue, 7: igualA, 8:igualacion } 
    valido = operaciones[op](op, operando1, operando2)
    return valido   

#1000 entero
#1500 decimal
#2000 boolean
#2500 frase string


def tipotemp(): #regresa el tipo nuevo de la variable temporal que sera creada
    global tipo
    return tipo