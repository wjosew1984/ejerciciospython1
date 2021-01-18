#Una compañía de helados ha creado un código para que se le introduzca el saber del helado y automáticamente indique el precio: 12. Funciones
def precio(sabor):
    if sabor == "chocolate":
        precio = 1.99
    else:
        precio = 2.49
    return precio
"""
Respecto al ejercicio anterior, ¿qué se mostrará por pantalla con
las siguientes instrucciones?
"""
#a. 
print(precio("banana")) 
2.49
#b. 
print(precio("chocolate")) 
1.99
#c. 
print(precio("vainilla")) 
2.49
#3. Crea una función llamada dibuja_triangulo de manera que automáticamente dibuje un triangulo.
def dibuja_triangulo(medida):
    for n in range (3):
        forward (medida)
        left (120)
