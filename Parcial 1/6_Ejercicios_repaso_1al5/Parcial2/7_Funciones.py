#una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. la funcion se puede reutilizar con el simple hecho de invocarla es decir mandarla llamar

Sintaxis:

def nombredemifuncion (parametros):
    bloque o conjunto de instrucciones 


    nombredemifuncion(parametros)

    Las funciones pueden ser de 4 tipos
    1.-Funcion que no recibe parametros y no regresa valor
    2.-Funcion que no recibe parametros y regresa valor 
    3.-Funcion que recibe parametros y no regresa Valor
    4.-Funcion que recibe parametros y regrese valor



    #Ejemplo 1:Crear una funcion para imprimir nombres de personas
    #1.-Funcion que no recibe parametros y no regresa valor
    def solicitarnombres():
        nombre=input("ingresa el nombre de la persona:")

        SolicitarNombres():


     n1=int(input("numero #1:"))
     n2=int(input("numero #2:"))
     suma=n1+n2
     print(f"¨{n1}+{n2}={suma}")
    

     suma()
    
    #Ejemplo 3 sumar dos numeros
    #2.-Funcion que no recibe parametros y regresa valor
    def suma():
       n1=int(input("Numero #1:"))
       n2=int(input("numero #2:"))
       suma=n1+n2
       resultado="{n1}+{n2}={suma}"

       suma()
       print(f"La suma es:{resultado_suma}")

       #Ejemplo 4 sumar dos numeros
       #3.-Funcion que recibe parametros y no regresa valor
       def suma():
          n1=int(input("Numero #1:"))
          n2=int(input("numero #2:"))
          suma=n1+n2
          return suma 
       
       resultado_suma=suma()
       print(f"La suma es:{resultado_suma}")
       #Ejemplo5 sumar dos numeros
       #4.-Funcion que recibe parametros y regresa valor 
       def suma(num1,num2):
          suma=num1+num2
          return suma
       
       n1=int(input("numero #1:"))
       n2=int(input("numero #2:"))
       resultado_suma=suma(n1,n2)
       print(f"La suma es : (resultado_suma)")

       #ejemplo 6 crear un programa que solicite a traves de una funcion la siguiente informacion :Nombre del paciente,edad,estatura,tipo de sangre,utilizar los 4 tipos de funciones
       