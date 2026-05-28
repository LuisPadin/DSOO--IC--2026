class Biblioteca:
    def __init__(self):
        self.inventario = []
        self.socios = []        
        self.prestamos = []     

    def agregar_material(self, material):
        self.inventario.append(material)

    def mostrar_inventario(self):
        print("\n--- Inventario ---")
        if len(self.inventario) == 0:
            print("El inventario está vacío.")
        for item in self.inventario:
            print(item)

    def agregar_socio(self, socio):
        self.socios.append(socio)

    def mostrar_socios(self):
        print("\n--- Listado de Socios ---")
        if len(self.socios) == 0:
            print("No hay socios registrados.")
        for s in self.socios:
            print(s)

    def mostrar_habilitados(self):
        print("\n--- Socios Habilitados para Operar ---")
        hay_habilitados = False
        for s in self.socios:
            if s.habilitado:
                print(s)
                hay_habilitados = True
        if not hay_habilitados:
            print("No hay socios habilitados en este momento.")

    def realizar_prestamo(self, id_socio, id_material):
        socio_encontrado = None
        for s in self.socios:
            if s.id_socio == id_socio:  # Búsqueda exacta y tradicional
                socio_encontrado = s
                break

        if socio_encontrado == None:
            print("Error: Socio no encontrado.")
            return

        if socio_encontrado.habilitado == False:
            print("Error: El socio no está habilitado.")
            return

        for item in self.inventario:
            if item.id_material == id_material:
                if item.disponible:
                    nuevo_prestamo = Prestamo(socio_encontrado, item)
                    self.prestamos.append(nuevo_prestamo)
                    print("Éxito: Material prestado correctamente.")
                else:
                    print("Error: El material no está disponible.")
                return
        print("Error: Material no encontrado.")

    def realizar_devolucion(self, id_material):
        for p in self.prestamos:
            if p.material.id_material == id_material and p.activo:
                p.finalizar()
                self.prestamos.remove(p)  
                print("Éxito: El material ha sido devuelto.")
                return
        print("Error: No se encontró un préstamo activo para ese código.")

    def mostrar_prestamos_activos(self):
        print("\n--- Préstamos Activos ---")
        if len(self.prestamos) == 0:
            print("No hay préstamos activos.")
        for p in self.prestamos:
            print(p)

