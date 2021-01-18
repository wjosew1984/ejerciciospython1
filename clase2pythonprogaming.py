"""
Ejercicio: Sucesión de Fibonacci
En matemática, se conoce a la “sucesión de
Fibonacci” como una sucesión infinita de números
naturales en la que cada término está
determinado por la suma de los dos términos
anteriores. Por ejemplo, empezando con el 0 y el
1, los primeros 20 términos son los siguientes:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
610, 987, 1597, 2584, 4181
Crear una función en Python que tome como
argumento un entero que indique la cantidad de
términos y retorne una lista como la anterior:
>>> fib(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
La función debe, además, chequear que
el argumento pasado sea mayor a 2. En
caso de ser menor, debe mostrar un
mensaje en pantalla y no retornar nada.
>>> fib(1)
La cantidad debe ser mayor a 2.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fib(cantidad):
    # Chequear que la cantidad sea un valor válido.
    if cantidad <= 2:
        print("La cantidad debe ser mayor a 2.")
        # Terminar la función.
        return
    # Esta es la lista que vamos a retornar. Por definición empieza
    # con los términos 0 y 1.
    ret = [0, 1]
    # Añadir elementos hasta haber alcanzado la cantidad indicada.
    while len(ret) < cantidad:
        # Agregamos al final de la lista un elemento que es la suma
        # de los dos anteriores.
        ret.append(ret[-1] + ret[-2])
    return ret


fib(1)
print(fib(15))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
def multiplos(maximo):
    """
    Ejercicio: Obtener múltiplos
    Escribir una función que, dado un número máximo,
retorne una lista con todos los números desde 1 hasta
dicho número que sean simultáneamente múltiplos
de 3 y de 5 (usar la operación resto con el carácter %).
>>> multiplos(100)
[15, 30, 45, 60, 75, 90]
    Retorna una lista con números que simultáneamente son múltiplos
    de 3 y 5, hasta un valor máximo especificado.
    """
    # Lista a retornar.
    ret = []
    # Recorrer una lista con todos los números desde el 1 hasta
    # el máximo indicado.
    for numero in range(1, maximo + 1):
        # Chequear que la división por 3 y 5 del número actual
        # sea exacta.
        if numero % 3 == 0 and numero % 5 == 0:
            ret.append(numero)
    return ret


print(multiplos(100))