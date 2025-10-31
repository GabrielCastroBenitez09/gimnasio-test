class Membresia:
    def __init__(self,
                precio_mensual = 75000,
                limite_reservas_por_semana = 3,
                zona_VIP = False,
                descuentos = "Ninguno",
                bebidas_gratis = "Ninguna"):
        self.precio_mensual = precio_mensual
        self.limite_reservas_por_semana = limite_reservas_por_semana
        self.zona_VIP = zona_VIP
        self.descuentos = descuentos
        self.bebidas_gratis = bebidas_gratis
    def __str__(self):
        return f"""
        {self.__repr__()}.
        -Tiene un precio mensual de {self.precio_mensual}.
        -{self.limite_reservas_por_semana} es el límite de reservas por semana disponibles.
        -Descuentos: {self.descuentos}.
        -Bebidas gratis: {self.bebidas_gratis}."""
    def __repr__(self):
        return "Membresía"

class MembresiaEstandar(Membresia):
    def __init__(self,
                 precio_mensual = 75000,
                limite_reservas_por_semana = 3,
                zona_VIP = False,
                descuentos = "Descuentos de temporada",
                bebidas_gratis = "Agua"):
        super().__init__(precio_mensual,
                         limite_reservas_por_semana,
                         zona_VIP,
                         descuentos,
                         bebidas_gratis)
        def __repr__(self):
            return "Membresía Estándar"

class MembresiaPremium(Membresia):
    def __init__(self,
                 precio_mensual = 75000,
                limite_reservas_por_semana = 8,
                zona_VIP = False,
                descuentos = "Descuentos de temporada y clases más baratas",
                bebidas_gratis = "Agua, Gatorade y RedBull"):
        super().__init__(precio_mensual,
                         limite_reservas_por_semana,
                         zona_VIP,
                         descuentos,
                         bebidas_gratis)
    def __repr__(self):
        return "Membresía Premium"

class MembresiaEstudiante(Membresia):
    def __init__(self,
                 precio_mensual = 75000,
                limite_reservas_por_semana = 5,
                zona_VIP = False,
                descuentos = "Descuentos de temporada, descuento de estudiante y descuento de invitado",
                bebidas_gratis = "Agua, Gatorade y RedBull"):
        super().__init__(precio_mensual,
                         limite_reservas_por_semana,
                         zona_VIP,
                         descuentos,
                         bebidas_gratis)
    def __repr__(self):
        return "Membresía Estudiante"