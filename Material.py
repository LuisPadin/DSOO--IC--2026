class Material:

    def __init__(self, titulo, editorial, año):
        self.__class__.contador = self.__class__.contador + 1
        inicial = self.__class__.inicial
        numero = self.__class__.contador
        self.id_material = f"{inicial}-{numero}"
        self.titulo = titulo
        self.editorial = editorial
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
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{f'[{self.id_material}]':<6} {estado:<13} | "


class Libro(Material):
    contador = 0
    inicial = "L"

    def __init__(self, titulo, editorial, autor, año):
        super().__init__(titulo, editorial, año)
        self.autor = autor
        
    def __str__(self):
        a = super().__str__()
        return f"{a}Título: {self.titulo:<22} | Autor: {self.autor:<18} | Editorial: {self.editorial:<9} | Año: {self.año}"


class Revista(Material):
    contador = 0
    inicial = "R"

    def __init__(self, titulo, editorial, numero, año):
        super().__init__(titulo, editorial, año)
        self.numero = numero
        
    def __str__(self):
        a = super().__str__()
        nro_formateado = f"N° {self.numero}"
        return f"{a}Título: {self.titulo:<22} | : {nro_formateado:<25} | Editorial: {self.editorial:<9} | Año: {self.año}"


