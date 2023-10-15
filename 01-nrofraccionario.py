"""
Implementar la clase de los números fraccionarios. El constructor debe, por
defecto, poner el denominador =1 si sólo se pasa 1 parámetro. Eso permite
representar los números enteros como fracciones.
a. Implementar la suma, resta, multiplicación y división.
b. Si el resultado de las operaciones es «simplificable», aplicar el algoritmo
de Euclides para obtener el resultado simplificado (investigue).
"""

class Fraccion:
    def __init__(self, numerador, denominador=1):
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def __str__(self):
        return str(self.numerador) + "/" + str(self.denominador)

    def __add__(self, other):
        return Fraccion(self.numerador * other.denominador + other.numerador * self.denominador, self.denominador * other.denominador)
    
    def __sub__(self, other):