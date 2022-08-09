#Nos pide un texto y que letra del texto quiere que cuente

n1=str(input("Ingrese una frase: "))
n2=str(input("Ingrese caracter para contar: "))
n3=n1.count(n2)
print("Se repite ",n3, "veces")
