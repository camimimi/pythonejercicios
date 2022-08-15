#Crea un patrón con números

#Pedimos un numero
x = int(input("Ingrese un número: "))
#Le indicamos al programa que imprimiremos el numero verticalmente, desde el 0 hasta que lleguemos al numero indicado
for i in range (0,x):
  #Le indicamos al programa que cuando estemos imprimiendo el programa verticalmente, le agregaremos uno más
  for n in range (0, i+1):
    #Imprimimos
    print (x, end="")
  print ()
