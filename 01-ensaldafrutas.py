"""
Defina una clase EnsaladaFrutas con un atributo frutas que sea inicialmente
[’melones’, ’piñas’, ’manzanas’] y un atributo raciones cuyo valor inicial sea 4.
Escriba un método __init__ que reciba los argumentos frutas (una lista de
cadenas) y raciones (un entero) guardando los valores obtenidos en los
atributos correspondientes.
a. Agregue un método que imprima el número de raciones restantes y las
frutas en la ensalada de frutas. La cadena debe verse como: “2 raciones
en la ensalada de [’platanos’, ’manzanas’]”.
b. Agregue un método agregar() que obtenga una cadena de texto y la
agregue al final de la lista frutas. Agregue además un método servir()
que reduzca en uno la cantidad de raciones e imprima “Disfrute”, si ya
no hay raciones debe imprimir “Disculpe”.
"""

class EnsaladaFrutas:
    def __init__(self, frutas, raciones):
        self.frutas = frutas
        self.raciones = raciones
    
    def print(self):
        print(self.raciones, "raciones en la ensalada de", self.frutas)
    
    def agregar(self, fruta):
        self.frutas.append(fruta)
    
    def servir(self):
        if self.raciones > 0:
            self.raciones -= 1
            print("Disfrute")
        else:
            print("Disculpe")

ensalada = EnsaladaFrutas(["melones", "piñas", "manzanas"], 4)
ensalada.print()
ensalada.agregar("naranjas")
ensalada.print()
ensalada.servir()
ensalada.print()
ensalada.servir()
ensalada.print()
ensalada.servir()
ensalada.print()
ensalada.servir()
ensalada.print()
ensalada.servir()