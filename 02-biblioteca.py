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


