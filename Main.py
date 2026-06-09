from Biblioteca import Biblioteca
from Material import Libro, Revista      
from Socio import Socio
from Datos import cargar_datos
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear') 

def pausar():
    input("\nPresione ENTER para continuar...")

def menu_principal():
    biblioteca = Biblioteca()
    cargar_datos(biblioteca)
    
    while True:
        cls()
        print("\n      SISTEMA BIBLIOTECA      \n")
        print("  1 | Agregar Libro o Revista")
        print("  2 | Agregar Socio")
        print("  3 | Ver Inventario")
        print("  4 | Prestamo o Devolución")
        print("  5 | Consultar Historial de Préstamos")
        print("  6 | Gestión de Socios")
        print("  0 | Salir")
        print("")
        print("=======================================")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            cls()
            print("    AGREGAR NUEVO MATERIAL    \n")
            print("1 | Libro")
            print("2 | Revista")
            print("=======================================")
            tipo = input("Seleccione tipo: ").strip()
            
            if tipo == "1" or tipo == "2":
                cls()
                try:
                    titulo = input("Título: ").strip()
                    editorial = input("Editorial: ").strip()
                    if tipo == "1":
                        autor = input("Autor: ").strip()
                        año = int(input("Año de publicación: "))
                        nuevo = Libro(titulo, autor, editorial, año)
                    else:
                        editorial = editorial = input("Editorial: ").strip()
                        edicion = int(input("Número de edición: "))
                        año = int(input("Año: "))
                        nuevo = Revista(titulo, edicion, editorial, año)
                    
                    es_nuevo = biblioteca.agregar_material(nuevo)
                    print("\n---------------------------------------")
                    if es_nuevo:
                        print(f" Nuevo material registrado:\n    '{titulo}'")
                    else:
                        print(f" Se sumó 1 unidad a:\n    '{titulo}'")
                    print("---------------------------------------")
                    
                except ValueError:
                    print("\n Dejo un campo vacio.")
                    
            else:
                print("\n  Opción inválida.")
            pausar()
                
        elif opcion == "2":
            cls()
            print("    REGISTRAR NUEVO SOCIO    \n")
            nom = input("Nombre y Apellido: ").strip()
            dni = "" 
            while len(dni) != 8 or not dni.isdigit():
                dni = input("Introduce el DNI (8 números exactos): ").strip()
                if len(dni) >= 8: 
                    dni = dni[0:8]
            biblioteca.agregar_socio(Socio(nom, dni))
            print(f"\n  Socio '{nom}' registrado correctamente.\n")
            pausar()
    
        elif opcion == "3":
            cls()
            print("    INVENTARIO \n")
            print("1 | Ver Libros")
            print("2 | Ver Revistas")
            print("3 | Ver Todo")
            print("")
            a = input("Seleccione opción: ").strip()
            cls()
            
            if a == "1" or a == "3":
                print("\n    LIBROS    ")
                encontro = False
                for l in biblioteca.inventario:
                    if l.id_material[0] == "L":
                        print(f"  {l}")
                        encontro = True
                if not encontro: 
                    print("  No hay libros registrados.")
            
            if a == "2" or a == "3":
                print("\n     REVISTAS    ")
                encontro = False
                for r in biblioteca.inventario:
                    if r.id_material[0] == "R":
                        print(f"  {r}")
                        encontro = True
                if not encontro: 
                    print("  No hay revistas registradas.")
            pausar()
                
        elif opcion == "4":
            cls()
            print("    GESTIÓN DE PRESTAMOS Y DEVOLUCIONES    \n")
            print("1 | Realizar Prestamo")
            print("2 | Realizar Devolucion")
            print("")
            a = input("Seleccione una opción: ").strip()
            
            if a == "1":
                cls()
                biblioteca.mostrar_socios()
                socio_id = input("Ingrese el ID del socio: ").strip()
                cls()
                
                biblioteca.mostrar_inventario()
                print("")
                mat_cod = input("Ingrese el ID del material (Ej: L1 o L-1): ").strip().upper()
                
                if len(mat_cod) >= 2 and "-" not in mat_cod:
                    mat_cod = f"{mat_cod[0]}-{mat_cod[1:]}"
                
                biblioteca.realizar_prestamo(socio_id, mat_cod)
                pausar()
            
            elif a == "2":
                cls()
                biblioteca.mostrar_prestamos_activos()
                print("")
                socio_id = input("Ingrese el ID del socio que devuelve: ").strip()
                mat_cod = input("ID del material a devolver (Ej: L1 o L-1): ").strip().upper()
                
                if len(mat_cod) >= 2 and "-" not in mat_cod:
                    mat_cod = f"{mat_cod[0]}-{mat_cod[1:]}"
                
                biblioteca.realizar_devolucion(socio_id, mat_cod)
                pausar()
            else:
                print("\n  Opción inválida.")
                pausar()
        
        elif opcion == "5":
            cls()
            print("    CONSULTA DE HISTORIAL    \n")
            print("1 | Ver Préstamos Activos")
            print("2 | Ver Préstamos Vencidos")
            print("3 | Total")
            print("")
            a = input("Seleccione una opción: ").strip()
            cls()
            
            if a == "1" or a == "3":
                print("    PRESTAMOS ACTIVOS VIGENTES    \n")
                for p in biblioteca.prestamos: 
                    if p.activo and not p.vencido():
                        print(f"  {p}")
                    
            if a == "2" or a == "3":
                print("\n    PRESTAMOS VENCIDOS    \n")
                for p in biblioteca.prestamos:
                    if p.vencido():
                        print(f"  {p}")
            pausar()

        elif opcion == "6":
            cls()
            print("    GESTIÓN DE ESTADO DE SOCIOS    \n")
            biblioteca.mostrar_socios()
            print("\n")
            print("1 | Habilitar Socio")
            print("2 | Deshabilitar Socio")
            print("")
            a = input("Seleccione una opción: ").strip()
            
            if a == "1" or a == "2":
                print("")
                id_buscado = input("Ingrese el ID del socio a modificar: ").strip()
                alta = True if a == "1" else False
                socio_modificado = biblioteca.estado_socio(id_buscado, alta)
                cls()
                print("\n")
                if socio_modificado:
                    estado_str = "HABILITADO" if alta else "SUSPENDIDO"
                    print(f"  ¡Cambio Guardado!\n    Socio: {socio_modificado.nombre}\n    Estado: {estado_str}")
                else:
                    print(" No se encontró ningún socio con ese ID.")
                print("")
            else:
                print("\n  Opción inválida.")
            pausar()

        elif opcion == "0":
            cls()
            print("\n      ¡Chau Crack!      \n")
            break
        else:
            print("\n  Opción no valida. Intente nuevamente.")
            pausar()

if __name__ == "__main__":
    menu_principal()
