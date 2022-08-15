#Calcula el volumen

#Pedimos el radio y la altura del cilindro
r = int(input("Ingrese el radio del cilindro: "))
h = int(input("Ingrese la altura del cilindro: "))
#Operamos en una variable el radio a la dos
d = r*r
#Hacemos la operacion para encontrar el volumen, la cual es pi que es 3.14, multiplicado por el cubo del radio, por la altura
V = 3.14 * d * h
#Imprimimos
print ("El volumen del cilindro es: ", V)
