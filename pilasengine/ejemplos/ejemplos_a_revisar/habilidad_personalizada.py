import pilasengine

class GirarPorSiempre(pilas.habilidades.Habilidad):

    def __init__(self, receptor):
        self.receptor = receptor

    def actualizar(self):
        self.receptor.rotacion += 1

pilas = pilasengine.iniciar()

a = pilas.actores.Mono()
a.aprender(GirarPorSiempre)
a.aprender(GirarPorSiempre)
a.aprender(GirarPorSiempre)
pilas.ejecutar()
