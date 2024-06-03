Print("Calculadora basica,escoge una opcion")
Opcion=input("/t.Elige una opcion:").upper()

if opcion==1.or.opcion="+" or opcion="SUMA"
    n1=int(input("numero.#1:."))
    n2=int(input("numero.#2:."))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

elif opcion=="2".or.opcion="-" or opcion=="RESTA"
    n1=int(input ("numero #1:"))
    n2=int(input("numero  #2:"))
    n3=int(input("numero  #3:"))
elif opcion=="3".or.opcion="*" or opcion=="MULTIPLICACION"

elif opcion=="4".or.opcion="/" or opcion=="DIVISION"


def solicitarNumero():
    n1=int("Numero #1: ")
    n2=int("Numero #2: ")

def operacionAritmetica(num1,num2,ope):
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
    return f"{n1}+{n2}={n1+n2}"
    elif



    def solicitarNumeros():
  global n1,n2  
  n1=int(input("Numero #1: "))
  n2=int(input("Numero #2: "))
  

def operacionAritmetica(num1,num2,opcion):  
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
      return f"{n1}+{n2}={n1+n2}"
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
     return f"{n1}-{n2}={n1-n2}"
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
     return f"{n1}*{n2}={n1*n2}"
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
     return f"{n1}/{n2}={n1/n2}"  
    else:  
     opcion=False    
     return "Terminaste la ejecucion del SW"

   system("clear") 
opcion=True    
while opcion:
 print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- SALIR ")
 opcion=input("\t Elige una opción: ").upper()

if opcion!=5:
 solicitarNumeros()
 print(operacionAritmetica(n1,n2,opcion))
