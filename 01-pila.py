"""
Cree una clase que implemente una pila, sus métodos (pop, push) y devuelva
cuantos ítems quedan en la pila.
"""

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):
        if self.Vacia():
            return None
        return self.items.pop()
    
    def Vacia(self):
        return self.items == []
    
    def tamaño(self):
        return len(self.items)
    
    def print(self):
        print(self.items)

pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.print()
print(pila.desapilar())
print(pila.desapilar())
print(pila.desapilar())
print(pila.desapilar())
pila.print()
print(pila.tamaño())
print(pila.Vacia())
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.print()
print(pila.tamaño())
