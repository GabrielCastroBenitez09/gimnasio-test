class Clase:
    def __init__(self, nombre_clase, id_clase, entrenador, horario, cupos, socios_inscritos):
        self.nombre_clase = nombre_clase
        self.id_clase = id_clase
        self.horario = horario
        self.cupos = cupos
        self.socios_inscritos = []
        if not isinstance(entrenador, Entrenador):
            raise ___Error("")
        else:
            self.entrenador = entrenador
    
    def reservar(self, socio):
        if isinstance(socio, Socio):
            self.socios_inscritos.append(socio)
            self.cupos -= 1
        else self.cupos == 0:
            raise CupoAgotadoError("Esta clase no tiene cupos disponibles")

    def cancelar(self, socio):
        self.socios_inscritos.remove(socio)
        self.cupos += 1

    def __repr__(self):
        return f""

class ClaseYoga(Clase):
    def __init__(self, nombre_clase, id_clase, entrenador, horario, cupos, socios_inscritos):
        super().__init__(nombre_clase, id_clase, horario, cupos, socios_inscritos)
        if entrenador.especialidad =="Yoga":
            self.entrenador = entrenador
        else:
            raise 

    def __repr__(self):
        return f""


class ClaseHIIT(Clase):
    def __init__(self, nombre_clase, id_clase, entrenador, horario, cupos, socios_inscritos):
        super().__init__(nombre_clase, id_clase, horario, cupos, socios_inscritos)

    def __repr__(self):
        return f""


class ClaseSpinning(Clase):
    def __init__(self, nombre_clase, id_clase, entrenador, horario, cupos, socios_inscritos):
        super().__init__(nombre_clase, id_clase, horario, cupos, socios_inscritos)

    def __repr__(self):
        return f""
    
    
    
    
    
    
    
    
    
    