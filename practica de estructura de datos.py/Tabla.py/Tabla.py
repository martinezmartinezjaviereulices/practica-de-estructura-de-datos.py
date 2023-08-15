#Ejercicio de practica 1
numero = float(input("Ingrese un número: "))
contador = 3

while contador <= 12:
    producto = numero * contador
    print ("{0} x {1} = {2}".format (numero,contador,producto))
    contador = contador + 2

#Ejercio de practica 2
numero = float (input("Ingresa un numero: "))
minimo = float (input("Desde donde desea mostrar: "))
maximo = float (input("Hasta donde desea mostrar: "))

for contador in range (minimo,maximo + 2):
    producto = numero * contador
    print ("{0} x {1} = {2}".format (numero,contador,producto))