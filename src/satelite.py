altitud_inicial = float(input("Ingrese la altitud inicial del satélite (en km): "))
coeficiente_arrastre = float(input("Ingrese el coeficiente de arrastre inicial (valor decimal pequeño, por ejemplo, 0.01): "))
altitud_minima = float(input("Ingrese la altitud mínima de seguridad (en km): "))

altitud_actual = altitud_inicial
numero_orbitas = 0
estabilizado = False

while altitud_actual > altitud_minima:
    altitud_perdida = coeficiente_arrastre * altitud_actual
    altitud_actual -= altitud_perdida
    coeficiente_arrastre += 0.0001 
    numero_orbitas += 1
    
    if altitud_perdida < 0.001:
        estabilizado = True
        break

if estabilizado:
    print("\nEl satélite se ha estabilizado en una órbita baja.")
    print(f"Altitud final: {altitud_actual:.2f} km")
    print(f"Número total de órbitas completadas: {numero_orbitas}")
else:
    print("\nEl satélite ha reingresado en la atmósfera terrestre y se ha desintegrado.")
    print(f"Número total de órbitas completadas: {numero_orbitas}")