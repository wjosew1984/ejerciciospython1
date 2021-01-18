"""
Capturar una excepción
Python cuenta con soporte de primer nivel para excepciones. Las excepciones son un
modelo para el manejo de errores. En otros lenguajes, como en C, se acostumbra a que las
funciones retornen un valor específico cuando ocurre algún error. El código que llama a
dicha función chequea el valor de retorno y toma las medidas necesarias. En Python,
cuando una función falla, en lugar de retornar un valor en particular lanza una excepción
(vía la palabra reservada raise). El código que invocó a dicha función puede implementar
un bloque para capturarla vía try y except.
Es posible definir excepciones o bien hacer uso de las que incorpora el lenguaje. Algunas
de ellas son: ValueError, TypeError, RuntimeError, KeyError (la convención de
nombramiento difiere de las funciones y otros objetos; en las excepciones cada término se
escribe con su primera letra en mayúscula y no se emplean guiones bajos). Por ejemplo,
int() sirve para convertir números de coma flotante y cadenas a su respectiva
representación númerica.
"""
import sqlite3

# Conectarse a la base de datos (se crea automáticamente si no existe).
conn = sqlite3.connect("productos.db")
cursor = conn.cursor()

# Crear la tabla.
cursor.execute(
    "CREATE TABLE productos (id NUMERIC, nombre TEXT, precio NUMERIC)")

# Añadir los productos.
productos = (
    (1, "Teclado", 500),
    (2, "Mouse", 350),
    (3, "Monitor", 1500),
    (4, "Parlantes", 1100),
)
for producto in productos:
    cursor.execute("INSERT INTO productos VALUES (?, ?, ?)", producto)

# Guardar los cambios.
conn.commit()

# Cerrar la conexión.
conn.close()