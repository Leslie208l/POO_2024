#Convertir los tipos de datos

#Nota: solo es posible en una concatenacion concatenar entre tipos de datos iguales

texto="Soy una cadena"
numero=23


print(texto+" y Soy una cadena2")
print(numero+34)


#Convertir un tipo de datos int a str
numero_str=str(numero)
print(texto+" "+numero_str)

print(texto+" "+str(numero)) #ES LA MAS COMUN PARA MOSTRAR UNA CADENA CON UN NUMERO

#CONVERTIR UN STR A INT
n1=33
suma=int('23')+n1
print("suma: "+str(suma))

#CONVERTIR UN float A INT
n1=33
n2=int(33.99)

suma=n1+n2
print(suma)

#CONVERTIR UN int A float

n1=3
n2=4

suma=float(n1+n2)

print(f"La suma es: {suma}")
print("La suma es: "+str(suma))