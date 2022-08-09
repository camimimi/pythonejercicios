#Cuenta las cosas en la lista y nos da la diferencia

f1=[1,3,4]
f2=[5,3,2]
f3=[10,5,7]

#Primero verificar si tienen el mismo largo
x= len(f1)
y= len(f2)
z= len(f3)

if x==y and x==z :
  f= f1[0]+ f1[-1]+f2[0]+ f2[-1]+f3[0]+ f3[-1]
  print(f)
  g= sum(f1)+sum(f2)+sum(f3)-f
  print(g)
  h= f-g
  print("El resultado es", h)
