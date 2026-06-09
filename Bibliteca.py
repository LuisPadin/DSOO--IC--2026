from Prestamo import Prestamo  

class Biblioteca:
    def __init__(self):
        self.inventario = []
        self.socios = []        
        self.prestamos = []     

    def agregar_material(self, material):
        for item in self.inventario:
            if item.titulo == material.titulo:
                item.stock = item.stock + 1
                return False
        self.inventario.append(material)
        return True

    def mostrar_inventario(self):
        print("\n     INVENTARIO      ")
        for material in self.inventario:
            if material.id_material[0] == "L":
                print(material)
            
        for material in self.inventario:
            if material.id_material[0] == "R":
                print(material)

    def agregar_socio(self, socio):
        self.socios.append(socio)

    def mostrar_socios(self):
        print("\n    LISTADO DE SOCIOS    ")
        if len(self.socios) == 0:
            print("No hay socios registrados.")
        for s in self.socios:
            print(s)

    def mostrar_habilitados(self):
        print("\n    SOCIOS HABILITADOS    ")
        hay_habilitados = False
        for s in self.socios:
            if s.habilitado:
                print(s)
                hay_habilitados = True
        if not hay_habilitados:
            print("No hay socios habilitados en este momento.")
    
    def estado_socio(self, id_socio, alta):
        id_buscado_str = str(id_socio).strip()
        for s in self.socios:
            if str(s.id_socio).strip() == id_buscado_str:
                s.habilitado = alta
                return s  
        return None  

    def realizar_prestamo(self, id_socio, id_material):
        socio_encontrado = None
        for s in self.socios:
            if s.id_socio == id_socio:  
                socio_encontrado = s
                break

        if socio_encontrado == None:
            return False

        if socio_encontrado.habilitado == False:
            return False

        for item in self.inventario:
            if item.id_material == id_material:
                if item.stock > 0:
                    nuevo_prestamo = Prestamo(socio_encontrado, item)
                    self.prestamos.append(nuevo_prestamo)
                    return True
                else:
                    return False
        return False

    def realizar_devolucion(self, id_socio, id_material):
        id_socio_str = str(id_socio).strip()
        for p in self.prestamos:
            if p.material.id_material == id_material and str(p.socio.id_socio).strip() == id_socio_str and p.activo:
                p.finalizar()  
                return True
        return False

    def mostrar_prestamos_activos(self):
        print("\n    PRESTAMOS ACTIVOS    ")
        if len(self.prestamos) == 0:
            print("No hay préstamos activos.")
        for p in self.prestamos:
            if p.activo:
                print(p)
