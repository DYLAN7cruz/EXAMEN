from usuario import Usuario

class Pelicula(Usuario):
    id                   = int
    nombre_pelicula      = str
    actores_principales  = str
    
    def __init__(self, id_usuario, nombre, id, nombre_pelicula, actores_princiáles):
        super().__init__(id_usuario, nombre)
        self.id                   = id
        self.nombre_pelicula      = nombre_pelicula
        self.actores_princiáles   = actores_princiáles

class MasInfo(Pelicula):
    calificacion  = int
    fecha_estreno = str

    def __init__(self, id_usuario, nombre, id, nombre_pelicula, actores_princiáles, calificacion, fecha_estreno):
        super().__init__(id_usuario, nombre, id, nombre_pelicula, actores_princiáles)
        self.calificacion   = calificacion
        self.fecha_estreno  = fecha_estreno

    def __str__(self):
        return f'La pelicula {self.nombre_pelicula} interpretada por {self.actores_principales} con una calificacion de {self.calificacion} estrellas, y estrenada {self.fecha_estreno} le corresponde el siguiente id:{self.id} Y fue vista por {self.nombre}{self.id_usuario}'

