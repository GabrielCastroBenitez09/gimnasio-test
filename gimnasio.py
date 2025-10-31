from datetime import datetime as dt
class Gimnasio():
    def __init__(self,socios,entrenadores,clases,pagos):
        self.socios= socios 
        self.entrenadores= entrenadores
        self.clases= clases
        self.pagos= pagos
    def __iter__(self):
        for c in self.clases:
            yield c
clases = {
    "Yoga": dt(2025, 11, 1,12,30),
    "Crossfit": dt(2025, 10, 31,8,0),
    "HIIT": dt(2025, 11, 2,15,0),
    "Yoga2": dt(2025,10,31,12,0)
}
G=Gimnasio(["Juan","Carlos","Sara"],{"Samuel":"Crossfit","Sarahy":"Yoga","Matias":"HIIT"},clases,True)
for clase in G:
    print(clase,G.clases[clase])


