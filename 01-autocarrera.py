"""
Crea una clase AutoCarreras que herede de una clase Auto sus atributos
(número de llantas, número de puertas, caballos de fuerza, velocidad, gasolina
en el tanque) y métodos (agregarGasolina, arrancarMotor) y agregue nuevos
atributos y métodos a elección.
a. Crea una clase Microbus que herede de la clase Auto anteriormente
mencionada sus atributos y métodos, y agregue nuevos atributos, y
métodos a elección.
b. Redefina el método arrancarMotor() para Microbus y AutoCarreras, de
manera de que impriman en pantalla, para cada caso, una cadena del
tipo "El microbus encendió el motor" o "El auto de carreras está listo
para avanzar usando 300 caballos de fuerza" (dónde caballos de fuerza
está definido para el objeto particular).
"""
class Auto:
    def __init__(self, ventanas):
        self.ventanas = ventanas

class AutoCarreras(Auto):
    def __init__(self, llantas, puertas, caballos, velocidad, gasolina):
        self.llantas = llantas
        self.puertas = puertas
        self.caballos = caballos
        self.velocidad = velocidad
        self.gasolina = gasolina

    def agregarGasolina(self, gasolina):
        self.gasolina += gasolina

    def arrancarMotor(self):
        print("El auto de carreras está listo para avanzar usando", self.caballos, "caballos de fuerza")

class Microbus(AutoCarreras):
    def __init__(self, llantas, puertas, caballos, velocidad, gasolina, pasajeros):
        super().__init__(llantas, puertas, caballos, velocidad, gasolina)
        self.pasajeros = pasajeros

    def arrancarMotor(self):
        print("El microbus encendió el motor")


auto = AutoCarreras(4, 1, 300, 0, 0)
microbus = Microbus(4, 2, 300, 0, 0, 20)
auto.arrancarMotor()
microbus.arrancarMotor()