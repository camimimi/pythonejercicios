#Un programa que solicite un número N y un número R y luego calcule la raíz R del número N y lo muestre en pantalla.

#Pedimos dos numeros
N = int(input("Ingrese número: "))
R = int(input("Ingrese número: "))
#Sacamos la raíz del primer numero, la raíz es el numero segundo
sqrt=N**(1/R)
print (sqrt)
