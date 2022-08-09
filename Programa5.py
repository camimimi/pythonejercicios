#Menu con 3 opciones, la primera para saber si dos personas son tocayas, otra opcion para sacar edades y la última para multiplicar

x=str(input("Hola! Escoge una opcion"))

h=str(input("a: tocayos, b: saber mi edad, c: multiplicando "))


a=str("Tocayos")
b=str("Saber mi edad")
c=str("Multiplicando")


if a:
  n1=str(input("ingrese nombre 1"))

  n2=str(input("ingrese nombre 2"))

  if n1==n2:
    print ("si son tocayos")
  else: 
    print ("no son tocayos")

  if b:
   n3=str(input("ingresa tu nombre"))
   print (n3)
   n4=float(input("ingresa tu año de nacimiento"))
   print (n4)
   n5 =float(input("ingresa año actual"))
   print (n5)
   res1=n4-n5
   print ("hola",n1, "tu tienes",res1,"años")

else:
    n6=int(input("pedir primer numero"))
    n7=int(input("pedir segundo numero"))
