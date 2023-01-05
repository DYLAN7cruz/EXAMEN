from usuario import Usuario
from pelicula import Pelicula
from pelicula import MasInfo
from director import Director
from categoria import Categoria
from informacion import Informacion

class Informacion2(Informacion):
    pais_origen1            = str
    vistas_mismoPais        = int
    

    def __init__(self,pais_origen, vistas, pelicula, director, usuario, categoria, pais_origen1, vistas_mismoPais ):
        self.pais_origen1
        self.vistas_mismoPais
     