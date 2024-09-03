

control= True

while control == True:
    print("1.Calcular primo\5\n2.Salir\3")
    opcion= int(input("ingrese la opción: "))
    if opcion == 1:
        numero = int(input("ingrese el numero a probar \1: "))
        cont = 0
        for divisor in range (1,numero+1):
            if (numero%divisor) == 0:
                cont += 1
        if cont > 2:
            print(f"{numero} no es primo")
        else:
            print(f"{numero} si es primo")
    elif opcion == 2:
        control = False
    else:
        print("opción no válida")
