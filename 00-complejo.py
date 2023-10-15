"""
Crea una clase Complejo que permita trabajar con números complejos (parte real y
parte imaginaria). Incluye los siguientes métodos: constructor (con todos los
parámetros), accedentes (funciones que retornen los valores de las variables de
entorno del objeto), mutadores (funciones que modifiquen las variables de
entorno del objeto), suma, resta, multiplicación, división y print() (función que
imprima los atributos del objeto).
"""

class Complejo:
    def __init__(self, real, imaginaria):
        self.real = real
        self.imaginaria = imaginaria

    def getReal(self):
        return self.real
    
    def getImaginaria(self):
        return self.imaginaria
    
    def setReal(self, real):
        self.real = real

    def setImaginaria(self, imaginaria):
        self.imaginaria = imaginaria

    def suma(self, complejo):
        return Complejo(self.real + complejo.getReal(), self.imaginaria + complejo.getImaginaria())
    
    def resta(self, complejo):
        return Complejo(self.real - complejo.getReal(), self.imaginaria - complejo.getImaginaria())
    
    def multiplicacion(self, complejo):
        return Complejo(self.real * complejo.getReal() - self.imaginaria * complejo.getImaginaria(), self.real * complejo.getImaginaria() + self.imaginaria * complejo.getReal())
    
    def division(self, complejo):
        return Complejo((self.real * complejo.getReal() + self.imaginaria * complejo.getImaginaria()) / (complejo.getReal()**2 + complejo.getImaginaria()**2), (self.imaginaria * complejo.getReal() - self.real * complejo.getImaginaria()) / (complejo.getReal()**2 + complejo.getImaginaria()**2))
    
    def print(self):
        print(self.real, "+", self.imaginaria, "i")


complejo1 = Complejo(1, 2)
complejo2 = Complejo(3, 4)
complejo1.print()
complejo2.print()
complejo1.suma(complejo2).print()
complejo1.resta(complejo2).print()
complejo1.multiplicacion(complejo2).print()
complejo1.division(complejo2).print()