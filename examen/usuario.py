class Usuario:
    id_usuario   = int
    nombre       = str

    def __init__(self, id_usuario, nombre):
        self.id_usuario  = id_usuario
        self.nombre       = nombre
        
    def __str__(self):
        return f'el id del usuario es el siguiente ¨{self.id_usuario} y su nombre es: {self.nombre}'
    
