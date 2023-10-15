"""
Considere el modelado de una biblioteca municipal, la cual contiene libros y revistas de
variadas colecciones. De acuerdo a este implemente lo siguiente:
A. Defina la clase Libro y Revista de acuerdo a las características más populares de estos y que
heredan de una clase común que es Documento que contiene sus atributos comunes, incluyendo
un atributo estado que indique si está prestado o no. Se deben incluír los métodos getters (que
retornan cada atributo (es uno por atributo)) y setters (que modifican cada atributo (es uno por
cada atributo)) donde correspondan (recuerde también que los métodos comunes deben estar
definidos de manera abstracta en la clase padre).
B. Considerando que un estante de libros se puede representar en una clase Estante, que puede
albergar una cierta cantidad de libros y revistas (en un arreglo), tiene un identificador, alberga
publicaciones de una sola categorización y además requiere los métodos listarDocumentos() que
muestra los títulos numerados (por índice en el arreglo) en orden de los libros en el estante y su
estado (prestado o no), prestarDocumento(n) que cambia el estado de un documento a prestado,
considerando su índice en el estante y regresarDocumento() que cambia el estado de un
documento a regresado, considerando su índice en el estante .
C. Genere un estante con al menos 10 libros y luego genere una interface que permita usar los
métodos de la clase Estante para el estante creado (usando un menú).
"""
import random

class Documento:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.estado = "Disponible"

class Libro(Documento):
    def __init__(self, titulo, autor, anio_publicacion, num_paginas):
        super().__init__(titulo, autor, anio_publicacion)
        self.num_paginas = num_paginas

class Revista(Documento):
    def __init__(self, titulo, autor, anio_publicacion, num_articulos):
        super().__init__(titulo, autor, anio_publicacion)
        self.num_articulos = num_articulos

class Estante:
    def __init__(self, identificador, categoria):
        self.identificador = identificador
        self.categoria = categoria
        self.documentos = []

    def listarDocumentos(self):
        for i, documento in enumerate(self.documentos):
            print(f"{i+1}. {documento.titulo} ({documento.anio_publicacion}) de {documento.autor}. Estado: {documento.estado}")

    def prestarDocumento(self, n):
        if n > 0 and n <= len(self.documentos):
            documento = self.documentos[n-1]
            if documento.estado == "Disponible":
                documento.estado = "Prestado"
                print(f"El documento {documento.titulo} ha sido prestado.")
            else:
                print(f"El documento {documento.titulo} no está disponible para ser prestado.")
        else:
            print("Índice de documento inválido.")

    def regresarDocumento(self, n):
        if n > 0 and n <= len(self.documentos):
            documento = self.documentos[n-1]
            if documento.estado == "Prestado":
                documento.estado = "Disponible"
                print(f"El documento {documento.titulo} ha sido regresado.")
            else:
                print(f"El documento {documento.titulo} no está prestado.")
        else:
            print("Índice de documento inválido.")

# Generar estante con 10 libros
estante = Estante("Estante 1", "Libros")
for i in range(10):
    libro = Libro(f"Título {i+1}", f"Autor {i+1}", random.randint(1900, 2021), random.randint(100, 500))
    estante.documentos.append(libro)


def mostrar_menu():
    print("Menú:")
    print("1. Ver Documentos")
    print("2. Prestar Documento")
    print("3. Regresar Documento")
    print("4. Salir")

while True:
    mostrar_menu()
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("Seleccionaste la Opción 1.")
        estante.listarDocumentos()
    elif opcion == "2":
        print("Seleccionaste la Opción 2.")
        n = int(input("Ingrese el índice del documento a prestar: "))
        estante.prestarDocumento(n)
    elif opcion == "3":
        print("Seleccionaste la Opción 3.")
        n = int(input("Ingrese el índice del documento a regresar: "))
        estante.regresarDocumento(n)
    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")


