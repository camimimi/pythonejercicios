#Te pide un número del 1 al 7 en representación a los días de la semana y luego dependiendo del número ingresado, te da un mensaje.

n1=int(input("ingrese un numero entre el 1 y el 7"))

if n1== 1:
  print ("¡Feliz lunes! Que tengas un buen inicio de semana :)")
elif n1== 2:
  print ("¡Feliz martes! Ten un buen día")
elif n1== 3:
  print ("¡Feliz miércoles! El ombligo de la semana, disfrutalo")
elif n1== 4:
  print ("¡Feliz jueves! Ya falta poco, no te desanimes")
elif n1== 5: 
  print("¡Feliz viernes! Estamos a nada del fin de semana")
elif n1== 6:
  print ("¡Feliz sábado! Pasa un buen fin de semana")
elif n1== 7: 
  print ("¡Feliz domingo! Descansa y preparate para iniciar una buena semana :)")
else:
  print("¡No le agregues más días a la semana!") 
