#Solicita al usuario un texto y muestra si es un palíndromo o no. 

#Pedimos un texto y quitamos los espacios
n1 = str(input("Ingrese un texto: "))
n2 = n1.replace (" ","")
print (n2)
#Ponemos el texto al reves y vemos si son palindromos o no
if str(n2) == "".join(reversed(n2)) :
    print("Palindromo")
else:
    print("No es Palindromo")
