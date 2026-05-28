class Socio:
    contador_socio = 0

    def __init__(self, nombre):
        Socio.contador_socio = Socio.contador_socio + 1
        self.id_socio = "Socio" + str(Socio.contador_socio)
        self.nombre = nombre
        self.habilitado = True

    def __str__(self):
        if self.habilitado:
            estado = "Habilitado"
        else:
            estado = "Suspendido"
        return "ID: " + self.id_socio + " | Nombre: " + self.nombre + " | Estado: " + estado

