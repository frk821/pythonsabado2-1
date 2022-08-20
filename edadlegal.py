#Edad legal
#Entrada del Problema
edad = int(input("Ingresa tu edad : "))

#Proceso del Problema
if (edad>=0 and edad==14):
    print(f'Si su edad es {edad} es un Niño')
elif(edad>=15 and edad==28):
    print(f'Si su edad es {edad} es un Joven')
elif(edad>=29 and edad==60):
    print(f'Si su edad es {edad} es un Adulto')
elif(edad>=61 and edad==99):
    print(f'Si su edad es {edad} es un Adulto Mayor')
elif(edad>99):
    print("Usted es una Momia")
else:
    print("Ingresa una opción válida")