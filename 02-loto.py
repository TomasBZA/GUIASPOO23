"""
Considere el famoso juego del loto, juego en que cada cartilla tiene 6 números de 36 posibles
(1,2,...,36). De acuerdo a lo anterior:
A. Defina la clase Loto que define un sorteo del loto, considerando los atributos:
 sorteo (una matriz que simboliza a todos los cartones de loto vendidos, considerando los
números jugados en cada cartón)
 ganadores (que simboliza la combinación de números ganadores).
Y los métodos:
 Init: que crea un objeto pidiendo el dato n (número de jugadores) y con esto, genera n
cartillas de loto que guarda como matriz en sorteo y genera una cartilla ganadora que
guarda en ganadores. Esto lo realizará utilizando el método siguiente.
 generar_cartilla(n: int) la cual retorna un arreglo de n cartillas del loto generadas
aleatoriamente.
 verificar_aciertos(n: int) la cual retorna la cantidad de cartillas en sorteo que poseen la
cantidad de aciertos indicadas.
B. Considerando esta definición de clase, utilícela para obtener los siguientes resultados:
De acuerdo a las funciones anteriores, genere un sorteo del loto de 10000 cartillas donde se
realice un reporte con la cantidad de apostadores con: 6, 5, 4 y 3 puntos respectivamente.
"""
import random

class Loto:
    def __init__(self, n):
        self.sorteo = self.generar_cartilla(n)
        self.ganadores = self.generar_cartilla(1)[0]

    def generar_cartilla(self, n):
        cartillas = []
        for i in range(n):
            cartillas.append(random.sample(range(1, 37), 6))
        return cartillas
    
    def verificar_aciertos(self, n):
        aciertos = 0
        for cartilla in self.sorteo:
            if len(set(cartilla) & set(self.ganadores)) == n:
                aciertos += 1
        return aciertos
    
sorteo = Loto(10000)
print("apostador con 6 pts:",sorteo.verificar_aciertos(6))
print("apostador con 5 pts:",sorteo.verificar_aciertos(5))
print("apostador con 4 pts:",sorteo.verificar_aciertos(4))
print("apostador con 3 pts:",sorteo.verificar_aciertos(3))
