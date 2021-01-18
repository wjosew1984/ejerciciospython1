#El bucle “while” ejecuta una porción de código mientras (while, en inglés) se cumpla una determinada condición.
a = 1
while a <= 10:
    print(a)
    a +=1
"""
El código imprime en pantalla los números del 1 al 9 ya
que, según la condición, el bucle debe ejecutarse siempre
que a sea menor a 10. En cada ejecución utiliza la función
incorporada print() para enviar un mensaje a la pantalla y la
sentencia a += 1 para incrementar el valor de a en 1 (es
equivalente a a = a + 1). Si hubiésemos omitido esta última
línea, el código imprimiría 1 en pantalla infinitamente.
"""