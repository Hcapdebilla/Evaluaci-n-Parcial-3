import json

def mostrar_menu():
    print("  [--------------------------]    ")
    print("     Bienvenido a SurExplora")
    print("  [--------------------------]    ")
    print("1. Registrar Reserva")
    print("2. Lista de Todas las Reservas")
    print("3. Imprimir Detalles de Reservas por Destino")
    print("4. Salir del Programa")

def registrar_reserva(reservas):
    nombre = input("Ingrese el nombre y apellido del cliente: ")
    ciudad = input("Ingrese la ciudad de origen: ")
    print("  [--------------------------]    ")
    print("       Seleccione el tour:")
    print("  [--------------------------]    ")
    print("1. Torres del Paine")
    print("2. Carretera Austral")
    print("3. Chiloé")
    
    tour_opcion = input("Ingrese la opción del tour (1-3): ")
    if tour_opcion == '1':
        tour = "Torres del Paine"
    elif tour_opcion == '2':
        tour = "Carretera Austral"
    elif tour_opcion == '3':
        tour = "Chiloé"
    else:
        print("Opción no válida")
        return

    try:
        cantidad_personas = int(input("Ingrese la cantidad de personas: "))
    except ValueError:
        print("Debe ingresar un número válido para la cantidad de personas")
        return

    if not nombre or not ciudad or not tour:
        print("Todos los datos son obligatorios")
        return

    reserva = {
        "nombre": nombre,
        "ciudad": ciudad,
        "tour": tour,
        "cantidad_personas": cantidad_personas
    }
    
    reservas.append(reserva)
    print("Reserva registrada exitosamente")

def listar_reservas(reservas):
    if not reservas:
        print("No hay reservas registradas")
        return
    
    print("\nLista de todas las reservas:")
    for reserva in reservas:
        print(f"Cliente: {reserva['nombre']}")
        print(f"Ciudad de Origen: {reserva['ciudad']}")
        print(f"Tour: {reserva['tour']}")
        print(f"Cantidad de Personas: {reserva['cantidad_personas']}")

def imprimir_detalle_por_destino(reservas):
    if not reservas:
        print("No hay reservas registradas")
        return

    destinos = ["Torres del Paine", "Carretera Austral", "Chiloé"]
    print("Seleccione el destino:")
    for i, destino in enumerate(destinos, 1):
        print(f"{i}. {destino}")
    
    destino_opcion = input("Opción del destino (1-3): ")
    if destino_opcion in ['1', '2', '3']:
        destino = destinos[int(destino_opcion) - 1]
    else:
        print("Opción no válida")
        return

    destino_reservas = [reserva for reserva in reservas if reserva['tour'] == destino]
    
    if not destino_reservas:
        print(f"No hay reservas para el destino: {destino}")
        return
    
    # Generar archivo .txt
    with open(f"{destino}_reservas.txt", "w") as txt_file:
        for reserva in destino_reservas:
            txt_file.write(f"Cliente: {reserva['nombre']}\n")
            txt_file.write(f"Ciudad de Origen: {reserva['ciudad']}\n")
            txt_file.write(f"Cantidad de Personas: {reserva['cantidad_personas']}\n")

    # Generar archivo .json
    with open(f"{destino}_reservas.json", "w") as json_file:
        json.dump(destino_reservas, json_file, indent=4)
    
    print(f"Detalle de reservas para {destino} ha sido generado en {destino}_reservas.txt y {destino}_reservas.json")

def main():
    reservas = []
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            registrar_reserva(reservas)
        elif opcion == '2':
            listar_reservas(reservas)
        elif opcion == '3':
            imprimir_detalle_por_destino(reservas)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor seleccione nuevamente.")

if __name__ == "__main__":
    main()