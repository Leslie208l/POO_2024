


#Ejemplo 3 crear un programa que solicite un numero entero y apartir de este numero genere e imprima la tabla de multiplicar correspondiente

numero=int(input("Ingrese un numero:"))

multi=0
i=1
while i<=10:
    multi=numero*i
    print(f"{numero} x {i} = {multi}")
    i+=1
