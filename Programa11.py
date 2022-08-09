#Pide el ingreso de dos nombres y busca si hay coincidencias.

n1=str(input("ingrese el primer nombre "))
n2=str(input("ingrese el segundo nombre "))
l1=int(len(n1)-1)
l2=int(len(n2)-1)

if n1 [0] == n2[0]:
  print ("Coincidencia")

elif n1 [l1] == n2[l2]:
  print("Coincidencia")

else:
  print ("No hay coincidencia")
