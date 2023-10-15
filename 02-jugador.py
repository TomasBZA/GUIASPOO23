"""
Clase Jugador:
Atributos: nombre: str, vida: int, estado: bool
Métodos:
shoot(jugador: Jugador): simula disparar al jugador indicado. Debe imprimir quién está disparando
y a quién dispara (usando los nombres de cada jugador). Utiliza la función dmg sobre el jugador
objetivo con un valor al azar entre 50 y 100.
info(): bool: indica los datos del jugador, imprimiendo su nombre y cantidad de vida.
Posteriormente imprime si el jugador está vivo o muerto, considerando el valor de su atributo
estado (si es True, está vivo y en False está muerto). Esta función, además, retorna el estado del
jugador como booleano.
heal(x:int): suma x a la cantidad actual de vida del jugador. El valor de vida del jugador no puede
sobrepasar 100, por lo que, si el jugador resulta con más vida al aplicar este método, debe
limitarlo a 100. Indica por pantalla qué jugador ganó vida y cuanta vida ganó
dmg(x: int): resta x a la cantidad actual de vida del jugador. El valor de vida del jugador no puede
ser menos que 0. Si tiene 0 puntos de vida o menos vida que 0, la cantidad de vida se limita a 0 y
su atributo estado cambia a False. Después de realizar esto se indica cuánto daño se realizó y si el
jugador tiene su estado en False, indica que el jugador ha muerto (indicando su nombre).
Considere todos los atributos de la clase privados y todos los métodos públicos.
Una vez terminado simular un duelo entre 3 jugadores creados con atributos a elección.
Comience mostrando la info de cada jugador.
Luego simule 10 llamadas a métodos a elección entre shoot y heal.
Termine mostrando la info de cada jugador e indicando, si hay un ganador (si sólo un jugador
queda vivo), quién es. En caso contrario, indicar que no hay ganadores.
"""
import random

class Jugador:
    def __init__(self, nombre: str, vida: int, estado: bool):
        self.nombre = nombre
        self.vida = vida
        self.estado = estado
    
    def shoot(self, jugador: 'Jugador'):
        print(f"{self.nombre} está disparando a {jugador.nombre}")
        dmg = random.randint(50, 100)
        jugador.dmg(dmg)
    
    def info(self) -> bool:
        print(f"Nombre: {self.nombre}")
        print(f"Vida: {self.vida}")
        if self.estado:
            print("Estado: Vivo")
        else:
            print("Estado: Muerto")
        return self.estado
    
    def heal(self, x: int):
        if self.vida + x > 100:
            ganancia = 100 - self.vida
            self.vida = 100
        else:
            ganancia = x
            self.vida += x
        print(f"{self.nombre} ha ganado {ganancia} puntos de vida")
    
    def dmg(self, x: int):
        self.vida -= x
        if self.vida < 0:
            self.vida = 0
            self.estado = False
            print(f"{self.nombre} ha muerto")
        else:
            print(f"{self.nombre} ha recibido {x} puntos de daño")

# Crear jugadores
jugadores = [Jugador("Jugador 1", 100, True), Jugador("Jugador 2", 100, True), Jugador("Jugador 3", 100, True)]

# Mostrar info de cada jugador
for jugador in jugadores:
    jugador.info()
