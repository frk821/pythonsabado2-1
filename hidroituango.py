#Entrada del Problema
nivelAgua = int(input("Ingresa el nivel de agua de presa: "))

#Proceso del Problema
if (nivelAgua>=0 and nivelAgua<20):
    print(f'El nivel de agua {nivelAgua} es muy bajo')
elif(nivelAgua>=20 and nivelAgua<400):
    print(f'El nivel de agua {nivelAgua} es óptimo')
elif(nivelAgua>=400):
    print(f'El nivel de agua {nivelAgua} es muy alto')
else:
    print("Ingresa una opción válida")