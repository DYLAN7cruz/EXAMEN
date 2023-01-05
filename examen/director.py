from usuario import Usuario

class Director(Usuario):
    lugar_nacimiento  = str
    genero            = str

    def __init__(self, id, nombre, lugar_nacimiento, genero):
        super().__init__(id, nombre)
        self.lugar_nacimiento  = lugar_nacimiento
        self.genero            = genero
