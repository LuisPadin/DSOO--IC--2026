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
        print("\n    INVENTARIO    ")
        for m in self.inventario:
            print(m)

    def agregar_socio(self, socio):
        self.socios.append(socio)

    def mostrar_socios(self):
        print("\n    LISTADO DE SOCIOS    ")
        if not self.socios:
            print("No hay socios registrados.")
        for s in self.socios:
            print(s)

    def mostrar_habilitados(self):
        print("\n    SOCIOS HABILITADOS    ")
        for s in self.socios:
            if s.habilitado:
                print(s)
    
    def estado_socio(self, id_socio, alta):
        id_buscado = str(id_socio).strip()
        for s in self.socios:
            if str(s.id_socio).strip() == id_buscado:
                s.habilitado = alta
                return s  
        return None  

    def realizar_prestamo(self, id_socio, id_material):
        id_material = str(id_material).upper().strip()
        if len(id_material) >= 2 and "-" not in id_material:
            id_material = f"{id_material[0]}-{id_material[1:]}"

        #  Buscar al socio
        socio_encontrado = None
        for s in self.socios:
            if str(s.id_socio).strip() == str(id_socio).strip():
                socio_encontrado = s

        # Si no existe o no está habilitado, no se puede prestar
        if socio_encontrado == None or not socio_encontrado.habilitado:
            print("Socio no válido o no habilitado.")
            return False

        # el material y registrar préstamo
        for m in self.inventario:
            if m.id_material == id_material and m.disponible:
                nuevo_prestamo = Prestamo(socio_encontrado, m)
                self.prestamos.append(nuevo_prestamo)
                print("\n")
                print(" Préstamo realizado.")
                return True
                
        print("Material no encontrado o no disponible.")
        return False

    def realizar_devolucion(self, id_socio, id_material):
        
        id_material = str(id_material).upper().strip()
        if len(id_material) >= 2 and "-" not in id_material:
            id_material = f"{id_material[0]}-{id_material[1:]}"
            
        id_socio_str = str(id_socio).strip()
        
        #  el préstamo activo que coincida
        for p in self.prestamos:
            if p.activo and p.material.id_material == id_material and str(p.socio.id_socio).strip() == id_socio_str:
                p.finalizar()  
                print("\n")
                print(" Devolución realizada.")
                return True
                
        print(" No se encontró ningún préstamo activo.")
        return False

    def mostrar_prestamos_activos(self):
        print("\n--- PRESTAMOS ACTIVOS ---")
        hay_activos = False
        for p in self.prestamos:
            if p.activo:
                print(p)
                hay_activos = True
                
        if not hay_activos:
            print("No hay préstamos activos.")
