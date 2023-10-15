"""
Cree una clase que implemente una cola, y sus métodos y devuelva cuantos
ítems quedan en la cola.
"""

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):
        if self.estaVacia():
            return None
        return self.items.pop(0)
    
    def estaVacia(self):
        return self.items == []
    
    def tamano(self):
        return len(self.items)
    
    def print(self):
        print(self.items)

cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.print()
print(cola.desencolar())
print(cola.desencolar())
print(cola.desencolar())
print(cola.desencolar())
cola.print()
print(cola.tamano())
print(cola.estaVacia())
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.print()
print(cola.tamano())