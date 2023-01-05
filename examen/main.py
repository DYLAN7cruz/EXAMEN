from usuario import Usuario
from pelicula import Pelicula
from pelicula import MasInfo
from director import Director
from categoria import Categoria
from informacion import Informacion
from informacion2 import Informacion2

if __name__ == "__main__":
    
    usuario3        =   Usuario(5, "BRYAN")
    usuario4        =   Usuario(12, "JUAN")

    pelicula1       =   MasInfo(345,"MARISOL",35,"TITANIC 2", "Leonardo DiCaprio, Kate Winslet, Gloria Stuart",5,"19/10/1997")   
    pelicula2       =   MasInfo(123,"FRANCISCO",22,"SOY LEYENDA 2", "Will Smith, Charlie Than",5,"14/10/2007")  

    pelicula3       =   Pelicula(123,"MARTA",22,"SOY LEYENDA", "Will Smith, Charlie Than")  

    categoria1      =   Categoria(345, "ROMANTICA")
    categoria2      =   Categoria(333, "TERROR")

    director1       =   Director("234", "James Cameron", "ESTADOS UNIDOS", "MASCULINO")
    director2       =   Director("234", "Francis Lawrence", "ESTADOS UNIDOS", "MASCULINO")

    usuario1        =   Usuario("234", "ERICK CRUZ")
    usuario2        =   Usuario("233", "DYLAN CRUZ")

    informacion1    =   Informacion("ESTADOS UNIDOS",123.222,pelicula1,categoria1,director1,usuario1)
    informacion2    =   Informacion("ITALIA",423.222,pelicula2,categoria2,director2,usuario2)
    
    informacion3    =   Informacion2("FRANCIA", 85858, pelicula1,categoria1,director1,usuario1, "QUITO", 8747)
    

    print("-------------------1---------------------")
    
    print(" ")
    print(usuario3)
    print(usuario4)
    print(vars(usuario4))
    print(" ")
    
    print("-------------------2---------------------")
    
    print(" ")
    print(vars(categoria1))
    print(" ")
    
    print("-------------------3---------------------")
    
    print(" ")
    print(pelicula1)
    print(" ")
    print(pelicula2)
    print(" ")
    
    print("-------------------4---------------------")
    
    print(" ")
    print("DIRECTOR")
    print(vars(director1))
    print(" ")
    
    print("-------------------5---------------------")
    
    print(vars(informacion3))
    print(" ")
    
    
    print("-------------------CLASE CON METODO---------------------")
    
    print("INFORMACION")
    print(vars(pelicula1))
    print(" ")
    print("PELICULA")
    print(vars(pelicula3))
    print(" ")
    print("CATEGORIA")
    print(vars(categoria1))
    print(" ")
    print("DIRECTOR")
    print(vars(director1))
    print(" ")
    print("USUARIO")
    print(vars(usuario1))

    

    print("-------------------OBJETOS DENTRO DE OBJETOS--------------")
    print(vars(informacion1))
    print(" ")
    print(vars(informacion2))
    

    

    
    
    
