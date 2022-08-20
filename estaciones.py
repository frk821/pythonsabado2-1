#Estaciones del año
#Entrada del Problema
mes = input("Ingresa el mes : ")

#Proceso del Problema
if (mes=='enero' or mes=='febrero' or mes=='marzo'):
    print(f'Si es {mes} estás en Invierno')
elif(mes=='abril' or mes=='mayo' or mes=='junio'):
    print(f'Si es {mes} estás en Primavera')
elif(mes=='julio' or mes=='agosto' or mes=='septiembre'):
    print(f'Si es {mes} estás en Verano')
elif(mes=='octubre' or mes=='noviembre' or mes=='diciembre'):
    print(f'Si es {mes} estás en Otoño')
else:
    print("Ingresa una opción válida")