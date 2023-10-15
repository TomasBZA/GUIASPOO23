"""
Crea una clase Rectangulo que modele rectángulos por medio de cuatro puntos
(los vértices). Dispondrá de dos constructores: uno que cree un rectángulo
partiendo de sus cuatro vértices y otro que cree un rectángulo partiendo de la
base y la altura, de forma que su vértice inferior izquierdo esté en (0,0). La clase
también incluirá un método para calcular la superficie y otro que desplace el
rectángulo en el plano. 
"""

class Rectangulo:
    def __init__(self, puntoA, puntoB, puntoC, puntoD):
        self.puntoA = puntoA
        self.puntoB = puntoB
        self.puntoC = puntoC
        self.puntoD = puntoD
    
    def __init__(self, base, altura):
        self.puntoA = Punto(0, 0)
        self.puntoB = Punto(base, 0)
        self.puntoC = Punto(base, altura)
        self.puntoD = Punto(0, altura)
    
    def getBase(self):
        return self.puntoB.getX()
    
    def getAltura(self):
        return self.puntoC.getY()
    
    def setBase(self, base):
        self.puntoB.setX(base)
        self.puntoC.setX(base)
    
    def setAltura(self, altura):
        self.puntoC.setY(altura)
        self.puntoD.setY(altura)
    
    def getSuperficie(self):
        return self.getBase() * self.getAltura()
    
    def desplazar(self, x, y):
        self.puntoA.setX(self.puntoA.getX() + x)
        self.puntoA.setY(self.puntoA.getY() + y)
        self.puntoB.setX(self.puntoB.getX() + x)
        self.puntoB.setY(self.puntoB.getY() + y)
        self.puntoC.setX(self.puntoC.getX() + x)
        self.puntoC.setY(self.puntoC.getY() + y)
        self.puntoD.setX(self.puntoD.getX() + x)
        self.puntoD.setY(self.puntoD.getY() + y)
    
    def print(self):
        print("[", end="")
        self.puntoA.print()
        print(",", end="")
        self.puntoB.print()
        print(",", end="")
        self.puntoC.print()
        print(",", end="")
        self.puntoD.print()
        print("]")

puntoA = Punto(0, 0)
puntoB = Punto(1, 0)
puntoC = Punto(1, 1)
puntoD = Punto(0, 1)
rectangulo = Rectangulo(puntoA, puntoB, puntoC, puntoD)
rectangulo.print()
rectangulo.setBase(2)
rectangulo.print()
rectangulo.setAltura(2)
rectangulo.print()
print(rectangulo.getSuperficie())
rectangulo.desplazar(1, 1)
rectangulo.print()
rectangulo = Rectangulo(1, 1)
rectangulo.print()
rectangulo.setBase(2)
rectangulo.print()
rectangulo.setAltura(2)
rectangulo.print()
print(rectangulo.getSuperficie())
rectangulo.desplazar(1, 1)
rectangulo.print()