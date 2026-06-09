from datetime import date, timedelta

class Prestamo:
    contador_prestamo = 0

    def __init__(self, socio, material, dias_prestamo=14):
        Prestamo.contador_prestamo = Prestamo.contador_prestamo + 1
        self.id_prestamo = str(Prestamo.contador_prestamo)
        self.socio = socio
        self.material = material
        self.activo = True
        self.material.prestar()
        self.fecha_inicio = date.today()
        self.fecha_vencimiento = self.fecha_inicio + timedelta(days=dias_prestamo)
     
    def vencido(self):
        return self.activo and date.today() > self.fecha_vencimiento

    def finalizar(self):
        self.activo = False
        self.material.devolver()

    def __str__(self):
        f_inicio = self.fecha_inicio.strftime("%d/%m/%Y")
        f_vence = self.fecha_vencimiento.strftime("%d/%m/%Y")
        if self.activo == False:
            estado = "Finalizado"
        elif self.vencido(): 
            estado = "¡VENCIDO!"
        else:
            estado = "Activo"
        
    
        return f"[N° {self.id_prestamo}] Socio: {self.socio.nombre} (ID: {self.socio.id_socio}) : {self.material.titulo} (ID Mat: {self.material.id_material}) | Retiro: {f_inicio} | Vence: {f_vence} ({estado})"
