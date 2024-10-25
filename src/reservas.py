import random

distancias = {
    ("Medellín", "Bogotá"): 240,
    ("Medellín", "Cartagena"): 461,
    ("Bogotá", "Cartagena"): 657
}

def calcu_prec(distancia, día):
    dia_semana = {True: 79900, False: 156900}
    finde = {True: 119900, False: 213000}
    enfinde = día.lower() in ["viernes", "sábado", "domingo"]
    cortadista = distancia < 400
    if enfinde:
        return finde[cortadista]
    return dia_semana[cortadista]

titulo = input("Ingrese su título (Sr. o Sra.): ")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
print(f"{titulo} {nombre} {apellido}, ¡Bienvenido a FastFast Airlines!\n")

print("Ciudades disponibles: Medellín, Bogotá, Cartagena")
origen = input("Seleccione su ciudad de origen: ")
destino = input("Seleccione su ciudad de destino: ")

if (origen, destino) not in distancias and (destino, origen) not in distancias:
    print("Origen y destino no válidos.")
else:
    dia_de_sem = input("Ingrese el día de la semana para viajar (por ejemplo, lunes): ")
    day_del_mes = int(input("Ingrese el día del mes para viajar (un número entre 1 y 30): "))
    
    distancia = distancias.get((origen, destino)) or distancias.get((destino, origen))
    
    ticket_price = calcu_prec(distancia, dia_de_sem)
    
    silla_pref = input("¿Prefiere un asiento en el pasillo, junto a la ventana, o sin preferencia? ").lower()
    letra_silla = "C" if "pasillo" in silla_pref else "A" if "ventana" in silla_pref else "B"
    numero_silla = random.randint(1, 29)
    asiento = f"{numero_silla}{letra_silla}"
    
    print("\n--- RESERVA COMPLETADA ---")
    print(f"Nombre: {titulo} {nombre} {apellido}")
    print(f"Origen: {origen}")
    print(f"Destino: {destino}")
    print(f"Fecha de vuelo: {dia_de_sem.capitalize()} {day_del_mes}")
    print(f"Precio del boleto: ${ticket_price}")
    print(f"Asiento asignado: {asiento}")