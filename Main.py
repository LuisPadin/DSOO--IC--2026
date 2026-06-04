from Biblioteca import Biblioteca
from Material import Libro, Revista      
from Socio import Socio

def menu_principal():
    biblioteca = Biblioteca()
    
   
    biblioteca.agregar_material(Libro("El Aleph", "Jorge Luis Borges", "2005"))
    biblioteca.agregar_material(Revista("National Geographic", 520, "2005"))
    biblioteca.agregar_socio(Socio("Juan Pérez"))

    while True:
        print("\n" )
        print(" ⚔️BIBLIOTECA⚔️ ")
        print("\n" )
        print("1| Alta de Material")
        print("2| Alta de Socio")
        print("3| Consultar Inventario")
        print("4| Registrar Préstamo")
        print("5| Registrar Devolución")
        print("6| Consultar Préstamos")
        print("7| Ver Listado de Socios")
        print("8| Ver Socios Habilitados")
        print("0| Salir")
        
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("¿Tipo de material? (1: Libro / 2: Revista): ")
            titulo = input("Título: ")
            if tipo == "1":
                autor = input("Autor: ")
                año = int(input( "Año: "))
                biblioteca.agregar_material(Libro(titulo, autor, año))
            elif tipo == "2":
                edicion = int(input("Número de edición: "))
                año = int(input( "Año: "))
                biblioteca.agregar_material(Revista(titulo, edicion, año))
            else:
                print("Opción inválida.")

        elif opcion == "2":
            nom = input("Nombre y Apellido del Socio: ")
            biblioteca.agregar_socio(Socio(nom))

        elif opcion == "3":
            biblioteca.mostrar_inventario()

        elif opcion == "4":
            # Ahora los IDs son números súper cortos
            socio_id = input("ID numérico del socio (Ej: 1): ")
            mat_cod = input("ID numérico del material (Ej: 1): ")
            biblioteca.realizar_prestamo(socio_id, mat_cod)

        elif opcion == "5":
            mat_cod = input("ID numérico del material a devolver (Ej: 1): ")
            biblioteca.realizar_devolucion(mat_cod)

        elif opcion == "6":
            biblioteca.mostrar_prestamos_activos()

        elif opcion == "7":
            biblioteca.mostrar_socios()

        elif opcion == "8":
            biblioteca.mostrar_habilitados()

        elif opcion == "0":
            print("¡Gracias por utilizar el sistema!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()
if __name__ == "__main__":
    menu_principal()
