entradasDispo = [1] * 100  
entradasVendi = [0] * 100  
precios = {
    "Platinum": 120000,
    "Gold": 80000,
    "Silver": 50000
}
asistentes = []  

print(" ")
print("Bienvenido a la compra de entradas // Creativos.cl")
print("EVENTO: Concierto VIP de Michael Jam")
print("SOLO 100 ASIENTOS")

def menu():
    print("MENU DE OPCIONES:")
    print(" ")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")

def compraEntradas():
    cantidad = int(input("Ingrese la cantidad de entradas a comprar (1 a 3): "))
    if cantidad < 1 or cantidad > 3:
        print("La cantidad ingresada es invalida.")
        return

    print("UBICACIONES DISPONIBLES")
    for i in range(0, 100, 10):
        fila = entradasDispo[i:i+10]
        fila_str = " ".join(["X" if x == 0 else str(x) for x in fila])
        print(f"Fila {i+1}-{i+10}: {fila_str}")

    for i in range(cantidad):
        ubicacion = int(input("Seleccione la ubicacion que desea (1-100): "))
        if ubicacion < 1 or ubicacion > 100 or entradasVendi[ubicacion-1] == 1:
            print("Ubicacion no disponible, intentelo de nuevo.")
            continue

        tipo_entrada = ""
        if ubicacion <= 20:
            tipo_entrada = "Platinum"
        elif ubicacion <= 50:
            tipo_entrada = "Gold"
        else:
            tipo_entrada = "Silver"

        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        rut = int(input("Ingrese su RUT (sin puntos ni guiones): "))
        entradasVendi[ubicacion-1] = 1
        entradasDispo[ubicacion-1] = 0  
        asistentes.append((nombre, apellido, rut, tipo_entrada))
        print("Su compra se ha realizado correctamente!")

def ubicacionesDispo():
    print("UBICACIONES DISPONIBLES: ")
    for i in range(0, 100, 10):
        fila = entradasDispo[i:i+10]
        fila_str = " ".join(["X" if x == 0 else str(x) for x in fila])
        print(f"Fila {i+1}-{i+10}: {fila_str}")

def listadoAsistentes():
    print(" ")
    print("LISTADO DE ASISTENTES: ")
    asistentes_ordenados = sorted(asistentes, key=lambda x: x[2])  
    for asistente in asistentes_ordenados:
        print(f"RUT: {asistente[2]}, Nombre: {asistente[0]}, Apellido: {asistente[1]}, Tipo Entrada: {asistente[3]}")   
    print(" ")

def gananciasTotales():
    total_entradas = {
        "Entrada Platinum": 0,
        "Entrada Gold": 0,
        "Entrada Silver": 0
    }
    totalGeneral = 0

    for asistente in asistentes:
        tipo_entrada = asistente[3]
        total_entradas[tipo_entrada] += 1
        totalGeneral += precios[tipo_entrada]
    
    print("\nTotal General: ", totalGeneral)

def salir():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    print(f"Gracias por gestionar tu entrada para Michael Jam!, {nombre} {apellido}.")
    print("Productora: Creativos.cl")

def principal():
    while True:
        menu()
        opcion = input("Ingrese una opcion (1 al 5): ")
        if opcion == "1":
            compraEntradas()
        elif opcion == "2":
            ubicacionesDispo()
        elif opcion == "3":
            listadoAsistentes()
        elif opcion == "4":
            gananciasTotales()
        elif opcion == "5":
            salir()
            break
        else:
            print("Opcion invalida. Intente nuevamente.")

principal()