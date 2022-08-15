#Programa para declarar si una oracion empieza con vocal o consonante

#Pedimos una palabra
h = str(input("Ingrese una palabra: "))
a = h[0]
#Declaramos nuestras variables con vocales y definimos si empieza con consonante o vocal
if a == "a" or a == "e" or a == "i" or a == "o" or a == "u" or a == "A" or a == "E" or a == "I" or a == "O" or a == "U":
  print ("Inicia con vocales")

else: 
  print ("Inicia con consonantes")
