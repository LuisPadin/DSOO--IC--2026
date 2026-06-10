from Prestamo import Prestamo  

class Biblioteca:
    def __init__(self):
        self.inventario = []
        self.socios = []        
        self.prestamos = []     

    def agregar_material(self, material):
        self.inventario.append(material)
        return True

    def mostrar_inventario(self):
        print("\n--- INVENTARIO ---")
        for m in self.inventario:
            print(m)

    def agregar_socio(self, socio):
        self.socios.append(socio)

    def mostrar_socios(self):
        print("\n--- LISTADO DE SOCIOS ---")
        if not self.socios: # Si la lista está vacía
            print("No hay socios registrados.")
        for s in self.socios:
            print(s)

    def mostrar_habilitados(self):
        print("\n--- SOCIOS HABILITADOS ---")
        for s in self.socios:
            if s.habilitado:
                print(s)
    
    def estado_socio(self, id_socio, alta):
        for s in self.socios:
            if s.id_socio == id_socio:
                s.habilitado = alta
                return s  
        return None  

    def realizar_prestamo(self, id_socio, id_material):
        socio_encontrado = None
        for s in self.socios:
            if s.id_socio == id_socio:
                socio_encontrado = s

        #Si no existe o no está habilitado, no se puede prestar
        if socio_encontrado == None or not socio_encontrado.habilitado:
            print("Socio no válido o no habilitado.")
            return False

        for m in self.inventario:
            if m.id_material == id_material and m.disponible:
                nuevo_prestamo = Prestamo(socio_encontrado, m)
                self.prestamos.append(nuevo_prestamo)
                print("Préstamo realizado con éxito.")
                return True
