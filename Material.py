class Material:
    contador_material = 0

    def __init__(self, titulo, año):
        Material.contador_material = Material.contador_material + 1
        self.id_material = str(Material.contador_material)
        self.titulo = titulo
        self.año = año
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self):
        self.disponible = True

    def __str__(self):
        if self.disponible:
            estado = "Disponible"
        else:
            estado = "Prestado"
        return "[" + self.id_material + "] " + self.titulo + " - " + estado

class Libro(Material):
    def __init__(self, titulo, autor, año):
        super().__init__(titulo, año)
        self.autor = autor
        
    def __str__(self):
        return super().__str__() + " | Tipo: Libro | Autor: " + self.autor + " | Año: " + str(self.año)

class Revista(Material):
    def __init__(self, titulo, numero, año):
        super().__init__(titulo, año)
        self.numero = numero
        
    def __str__(self):
        return super().__str__() + " | Tipo: Revista | N°: " + str(self.numero)  + " | Año: " + str(self.año)



