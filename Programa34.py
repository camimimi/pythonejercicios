#Solicita el nombre completo de una persona y generar un correo electrónico con su nombre basándose en las iniciales y el apellido del mismo para mostrarlo en pantalla.

#Pedimos los nombres y apellidos
nom = str(input("Ingrese su primer nombre: "))
nom1 = str(input("Ingrese su segundo nombre: "))
ap = str(input("Ingrese su primer apellido: "))
ap1 = str(input("Ingrese su segundo apellido: "))
l = "@baco.com"

a = nom[0]
b = nom1[0]
#Juntamos las partes y creamos el correo
h = a+b+ap+ap1+l
print ("Su correo sería:",h)
