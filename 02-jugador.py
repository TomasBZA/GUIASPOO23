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