#Imprime 2 patrones seguidos

print("Patron")

for i in range (0, 10):
 for j in range (0, i+1):
  print ( "* ", end="" )
 print()

for j in range (0, 10):
 for i in range (0, i):
  print ( "* ", end="" )
 print()
