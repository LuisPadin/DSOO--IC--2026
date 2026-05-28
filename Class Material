class Material:
    # Contador para materiales
    contador_material = 0

    def __init__(self, titulo):
        Material.contador_material = Material.contador_material + 1
        self.id_material = "MAT" + str(Material.contador_material)
        self.titulo = titulo
        self.disponible = True

# funciones clase Material 
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
    def __init__(self, titulo, autor):
        super().__init__(titulo)
        self.autor = autor
    def __str__(self):
        return super().__str__() + " | Tipo: Libro | Autor: " + self.autor

class Revista(Material):
    def __init__(self, titulo, numero):
        super().__init__(titulo)
        self.numero = numero
        

    def __str__(self):
        return super().__str__() + " | Tipo: Revista | N°: " + str(self.numero)

