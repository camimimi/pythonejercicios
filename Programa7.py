#Para saber si son mayores, menor o iguales

n1=int(input("ingrese el primer número"))
n2=int(input("ingrese el segundo número"))

if n1<n2:
  print ("El primer número es menor")
  if n2<n1:
   print ("El segundo número es menor")
else:
  print("Los numeros son iguales") 
