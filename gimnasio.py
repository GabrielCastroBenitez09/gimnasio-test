from datetime import datetime as dt
class Gimnasio():
    def __init__(self,socios,entrenadores,clases,pagos):
        self.socios= socios 
        self.entrenadores= entrenadores
        self.clases= clases
        self.pagos= pagos
    def __iter__(self):
        for c,f in sorted(self.clases.items(), key=lambda x: x[1]):
            yield c
    def __len__(self):
        return len(self.clases)
