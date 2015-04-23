
cont=1;
contemp=0;
cuadruplos[300][5];
cuadro = 2;
int i,j;


FILE *cuadf;
   Stack *PilaO;
   Stack *PSaltos;
   Stack *POper;
   void init() { 
   //Crear las pilas e inicializarlas
   //pila de operadores
      PilaO=createStack(100);//pila de operandos
      PSaltos=createStack(100);//pila de saltos
      POper=createStack(100);//pila de operadores
      	cuadf = fopen("Maquina/cuadruplos.txt", "w+");
      if (cuadf == NULL) {
         fprintf(stderr, "Archivo cuadruplos.txt no se ha podido abrir");
         exit(1);
      }
   }
 	 
def printcuadruplos():
  for i in range(300):
 	  for j in range(5):
 	    if cuadruplos[i][j]== 0:
        sys.exit(1);
      print( repr(cuadf), repr(cuadruplos[i][j]))
  
  print(repr(cuadf)) ;
  
#verificar dir como palabra resevada de python
def escribe_ctei(dir, val):
  print(repr(cuadf),"-1", repr(dir), repr(val))

def escribe_ctef(dir, val):
  print(repr(cuadf),"-1", repr(dir), repr(val))

def escribe_ctes(dir, val):
  print(repr(cuadf),"-1", repr(dir), repr(val))
  
  
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
  push(PilaO, oper)
  print(stderr, "Ya meti oper \n", repr(oper))
   
#2
def pila_op(int op):
    push(POper, op)
    print(stderr, "ya meti op \n", repr(op))
   
#3
def parentesisPush():
    push(POper, 11) #genera pared falsa en pila
   
def parentesisPop():
    pop(POper) #saca de la pila  
      
#5
def termino(): 
  print(stderr, "Estoy en cuadruplo termino\n");
  op = top(POper)
  pop(POper)
  if (op == 3 || op == 4):			#operadores * o /
    oper2 = top(PilaO) 
    pop(PilaO)
    oper1 = top(PilaO)
    pop(PilaO)
    if (check(op, oper1, oper2)):		#checa si es valido
      escribe_cuad(cont, op, oper1, oper2, contemp+tipotemp())	#genera el cuadruplo
      pila_id(contemp+tipotemp())			#mete el resultado a la pila de operadores
      contemp = contemp+1
    
    else		#marca error si no es compatible
      print(stderr, "***ERROR DE TIPOS**** termino\n")
      sys.exit(1)
  else
      fprintf(stderr, "No es termino pasar al siguiente \n")
      pila_op(op)
   
   //6
   void *expresion(){
      fprintf(stderr, "Estoy en cuadruplo expresion\n");
      int op = top(POper);
      pop(POper);
      if(op == 1 || op == 2){				//operadores + o -
         int oper2 = top(PilaO);
         pop(PilaO);
         int oper1 = top(PilaO);
         pop(PilaO);
         if(check(op, oper1, oper2)){		//checa el tipo    
            escribe_cuad(cont, op, oper1, oper2,  contemp+tipotemp());		//genera el cuadruplo
            pila_id(contemp+tipotemp());			//mete el resultado a la pila de operadores
            contemp++;
         }
         else{		//marca error si no es compatible
            fprintf(stderr, "***ERROR DE TIPOS**** expresion\n");
            exit(1);
         }
      }
      else{
         fprintf(stderr, "No es expresion pasar al siguiente \n");
         pila_op(op);}
     
   }
   
   //7
   void *relacional(){
      fprintf(stderr, "Estoy en cuadruplo relacional\n");
      int op = top(POper);
      pop(POper);
      if(op == 5 || op == 6 || op == 7 ){ // op == < || op == > || op = ==
         int oper2 = top(PilaO); 
         pop(PilaO);
         int oper1 = top(PilaO);
         pop(PilaO);
         if(check(op, oper1, oper2)){		//checa el tipo
            escribe_cuad(cont, op, oper1, oper2,  (contemp+tipotemp()));
            pila_id(contemp+tipotemp());			//mete el resultado a la pila de operadores
            contemp++;
         }
         else{		//marca error si no es compatible
           
            fprintf(stderr, "***ERROR DE TIPOS**** relacional\n");
            exit(1);
                  
         }
      }
      else{
         fprintf(stderr, "No es relacional pasar al siguiente \n");
         pila_op(op);
      }
   }
   
	//8
   void *assign(){
      fprintf(stderr, "Estoy en quad assign\n");
      int op = top(POper);
      pop(POper);
      if(op == 10){	//si el operador es =
         int oper2 = top(PilaO); 
         pop(PilaO); 
         int oper1 = top(PilaO);
         pop(PilaO);
         if(check(op, oper1, oper2)){	//checa el tipo
            escribe_cuad(cont, op,  oper2, -1, oper1);		//genera el cuadruplo
            contemp++;
          
         }
         else{		//marca error si no es compatible
            fprintf(stderr, "***ERROR DE TIPOS**** assign\n");
            exit(1);
         
            
         }
      }
      else{
         fprintf(stderr, "No es asignacion pasar al siguiente \n");
         pila_op(op);
      }
   }
    //15
   void *logico(){
      fprintf(stderr, "Estoy en cuad logico\n");
      int op = top(POper);
      pop(POper);
      if(op == 8 || op == 9){ // op == & || op == |
         int oper2 = top(PilaO);
         pop(PilaO);
         int oper1 = top(PilaO);
         pop(PilaO);
         if(check(op, oper1, oper2)){		//checa el tipo
            escribe_cuad(cont, op, oper1, oper2,  (contemp+tipotemp()));
            pila_id(contemp+tipotemp());			//mete el resultado a la pila de operadores
            contemp++;
         }
         else{		//marca error si no es compatible
            fprintf(stderr, "***ERROR DE TIPOS**** logico\n");
            exit(1);
         }
      }
      else{
         fprintf(stderr, "No es logico, pasar al siguiente \n");
         pila_op(op);
      }
   }
	
      
  //10
   void *if1()
   {
      fprintf(stderr, "Estoy en cuadruplo if\n");
     //if
     //1.- genera gotoF y mete cont-1 a la pila de saltos
      int op = 20;
      int oper1 = top(PilaO);
      if (oper1 < 10000|oper1>=11000)
         fprintf(stderr, "***ERROR DE TIPOS**** IF\n");
      else{
         pop(POper);
         escribe_cuad(cont, op, oper1, -1, -1);
       push(PSaltos, cont-1);
            }
   } 

   //11
	 void *else1()
   {
     //2genera goto (else), y saca falso de la pila y rellena el primer salto
      int op = 22;//goto
      escribe_cuad(cont, op, -1, -1, -1);
      int falso = top(PSaltos);
 cuadruplos[falso-1][4]=cont;
      push(PSaltos, cont-1);
   }
   //12
	   void *if2()
   {
      int fin=top(PSaltos);
      pop(PSaltos);
      cuadruplos[fin-1][4]=cont;
   
   } 
   //13
   void *do1()
   { 
     //do-while
     //1.- mete cont a pila de saltos
      push(PSaltos, cont);
     
     }
   //14
   void *do2()
   { 
     //2.- genra gotoV e incrementa el cont
      int op = 21; //gotov
      int oper1 = top(PilaO);
      int oper2 = -1;
      escribe_cuad(cont, op, oper1, -1, contemp);
    
   }
  
  void print(){
  int op=33;
  push(POper,op);}
  
  void print2(){
  int oper1=top(PilaO);
  escribe_cuad(cont,top(POper),oper1,-1,-1);
  }
  
  int cuadproc(){
  return cont;
  }


  
