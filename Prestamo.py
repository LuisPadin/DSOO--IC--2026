class Prestamo:
    contador_prestamo = 0

    def __init__(self, socio, material):
        # ID autoincremental numérico puro para el préstamo
        Prestamo.contador_prestamo = Prestamo.contador_prestamo + 1
        self.id_prestamo = str(Prestamo.contador_prestamo)
        self.socio = socio
        self.material = material
        self.activo = True
        self.material.prestar()

    def finalizar(self):
        self.activo = False
        self.material.devolver()

    def __str__(self):
        return "[Préstamo N° " + self.id_prestamo + "] Socio: " + self.socio.nombre + " (ID: " + self.socio.id_socio + ") -> Material: " + self.material.titulo
