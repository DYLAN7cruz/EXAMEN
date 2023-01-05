from usuario import Usuario
from pelicula import Pelicula
from pelicula import MasInfo
from director import Director
from categoria import Categoria

class Informacion:
    pais_origen   = str
    vistas        = int
    pelicula      = MasInfo("","","","","","","")
    director      = Director("","","","")
    usuario       = Usuario("","")
    categoria     = Categoria("","")

    def __init__(self, pais_origen, vistas, pelicula, director, usuario, categoria):
        self.pais_origen   = pais_origen
        self.vistas        = vistas
        self.pelicula      = pelicula
        self.director      = director
        self.usuario       = usuario
        self.categoria     = categoria