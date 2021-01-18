#1. Completa el código siguiente para que diga “¡Buenos días!” siempre y cuando se introduzca el nombre Ana.
nombre = input("Introduce tu nombre: ")
if nombre == "Ana":
    print ( "¡Buenos días!" )
#2. Completa el código siguiente para que diga “Coge un pastel” siempre y cuando se introduzca Pastel. De lo contrario haz que le ofrezca una Galleta.
comida = input("¿Cual es tu comida favorita? ")
if comida == "pastel":
    print (" Coge un pastel ")
else:
    print (" Coge una galleta ")