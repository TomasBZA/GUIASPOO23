"""
Defina la clase Punto, caracterizada por los atributos x e y representando las
coordenadas de un punto como (x,y). Considerando esta clase, defina una clase
Linea con dos atributos: puntoA y puntoB. Son dos puntos por los que pasa la línea
en un espacio de dos dimensiones. La clase dispondrá de los siguientes métodos:
a. __init__(PuntoA, PuntoB)
Constructor que recibe como parámetros dos objetos de la clase Punto,
que son utilizados para inicializar los atributos. Si no se pasan parámetros,
debe considerar que se definen sus dos puntos como (0,0) y (0,0).
b. mueveDerecha(int)
Desplaza la línea a la derecha la distancia que se indique.
c. mueveIzquierda(int)
Desplaza la línea a la izquierda la distancia que se indique.
d. mueveArriba(int)
Desplaza la línea hacia arriba la distancia que se indique.
e. mueveAbajo(int)
Desplaza la línea hacia abajo la distancia que se indique.
f. Accedentes (getters): métodos que retornan cada uno de los atributos de la
clase
g. mutadores (setters): métodos que modifican a través de uno o más
parámetros cada atributo de la clase.
h. Método que nos permita mostrar la información de la línea de la siguiente
forma:
[puntoA,puntoB]. Por ejemplo: [(0.0,0.0),(1.0,1.0)]. 
"""
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self, x):
        self.x = x
    
    def setY(self, y):
        self.y = y
    
    def print(self):
        print("(", self.x, ",", self.y, ")")

class Linea:
    def __init__(self, puntoA, puntoB):
        self.puntoA = puntoA
        self.puntoB = puntoB
    
    def mueveDerecha(self, distancia):
        self.puntoA.setX(self.puntoA.getX() + distancia)
        self.puntoB.setX(self.puntoB.getX() + distancia)
    
    def mueveIzquierda(self, distancia):
        self.puntoA.setX(self.puntoA.getX() - distancia)
        self.puntoB.setX(self.puntoB.getX() - distancia)
    
    def mueveArriba(self, distancia):
        self.puntoA.setY(self.puntoA.getY() + distancia)
        self.puntoB.setY(self.puntoB.getY() + distancia)
    
    def mueveAbajo(self, distancia):
        self.puntoA.setY(self.puntoA.getY() - distancia)
        self.puntoB.setY(self.puntoB.getY() - distancia)
    
    def getPuntoA(self):
        return self.puntoA
    
    def getPuntoB(self):
        return self.puntoB
    
    def setPuntoA(self, puntoA):
        self.puntoA = puntoA
    
    def setPuntoB(self, puntoB):
        self.puntoB = puntoB
    
    def print(self):
        print("[", end="")
        self.puntoA.print()
        print(",", end="")
        self.puntoB.print()
        print("]")

punto1 = Punto(0, 0)
punto2 = Punto(1, 1)
linea = Linea(punto1, punto2)
linea.print()
linea.mueveDerecha(1)
linea.print()
linea.mueveIzquierda(1)
linea.print()
linea.mueveArriba(1)
linea.print()
linea.mueveAbajo(1)
linea.print()
linea.setPuntoA(Punto(2, 2))
linea.setPuntoB(Punto(3, 3))
linea.print()
linea.getPuntoA().print()
linea.getPuntoB().print()
