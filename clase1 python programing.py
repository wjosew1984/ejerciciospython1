#a=2
#b=3
#c=a+b
#print(c)

# ~ nombre="Adrian"
# ~ apellido="Jusid"

# ~ print(nombre + " " + apellido)

# ~ edad=43

# ~ print("soy " + nombre + " y tengo " + str(edad) + "  años")

# ~ entero integer int
# ~ coma flotante float float
# ~ cadena de carácteres string str
# ~ booleanos boolean bool (True, False)

				# ~ and		or		not
# ~ True	True	True	True	False
# ~ True	False	False	True
# ~ False	True	False	True	True
# ~ False	False	False	False

# ~ num=int(input("Ingrese un número: "))
# ~ if num==100: 
	# ~ print("número igual a cien")
# ~ elif num > 100:
	# ~ print("número mayor a cien")
# ~ elif num > 100:
	# ~ print("número mayor a cien")
# ~ elif num > 100:
	# ~ print("número mayor a cien")	
# ~ else:
	# ~ print("número menor a cien")	

# ~ print("se ejecuta siempre, fuera del bloque")


# ~ tupla=(10,20,30,40,50,60)
# ~ print(tupla[3])
# ~ t1=(5,6)
# ~ t2=(7,8)
# ~ t3=t1+t2
# ~ print(t3)

# ~ lista=[10,20,30,40,50]
# ~ print(lista[2])
# ~ lista[2]=35
# ~ print(lista)

# ~ lista=[1,True,"Hola",34.5, (5,7), [34,45]]

# ~ lista=[10,20,30,40,50]

# ~ lista.append(60)
# ~ print(lista)
# ~ lista.insert(2,25)
# ~ print(lista)
# ~ del lista[2]
# ~ print(lista)
# ~ lista.remove(60)
# ~ print(lista)
# ~ quitado=lista.pop(4)
# ~ print(quitado)
# ~ print(lista)

# ~ print(len(lista))

# ~ lista=[10,20,30,40]

# ~ for numero in lista:
	# ~ print(numero)
	
# ~ for posicion in range(0,len(lista),1):
	# ~ print(lista[posicion])	
	
#lista=[10,20,30,40]?

# ~ lista=[]
# ~ valor=0
# ~ for i in range(0,4,1):
	# ~ valor+=10 #~valor=valor+10
	# ~ lista.append(valor)
# ~ print(lista)

# ~ lista=[]
# ~ for valor in range(10,50,10):
		# ~ lista.append(valor)
# ~ print(lista)



	
# ~ for contador in  range(0,5,1):
	# ~ print("hola")	
	

# ~ range(desde, hasta, incremento)

# ~ range(0,5,1) -> [0,1,2,3,4] ~ range(0,5) ~ range(5)
# ~ range(0,5,2) -> [0,2,4]
# ~ range(1,10,1) -> [1,2,3,4,5,6,7,8,9]
# ~ range(5,-1,-1) -> [5,4,3,2,1,0]


# ~ matriz=[["a","b","c"],["d","e","f"]]

# ~ print(matriz)



# ~ for lista in matriz:
	# ~ for elemento in lista:
		# ~ print(elemento)
	
# ~ for fila in matriz:
	# ~ for columna in fila:
		# ~ print(columna)
		
		

# ~ for fila in range(0,2,1):
	# ~ for columna in range(0,3,1):
		# ~ print(matriz[fila][columna])


#[[10,20,30],[40,50,60]]?

# ~ matriz=[]
# ~ valor=0
# ~ for fila in range(0,2,1):
	# ~ matriz.append([]) #[[]]
	# ~ #print(matriz)
	# ~ for columna in range(0,3,1):		
		# ~ valor=valor+10
		# ~ matriz[fila].append(valor)
# ~ print(matriz)	
		

#diccionario={clave1:valor1, clave2:valor2,...,claven:valorn}

# ~ alumno={"nombre":"Juan","cursos":2}

# ~ print(alumno["nombre"])
# ~ print(alumno["cursos"])

# ~ alumno["cursos"]=4
# ~ print(alumno)

# ~ alumno["curso_actual"]="Python"
# ~ print(alumno)

# ~ for clave in alumno:
	# ~ print(clave)

# ~ for clave in alumno:
	# ~ print(alumno[clave])

# ~ num=1
# ~ while num<10:
	# ~ print(num)
	# ~ num+=1
	# ~ if num==5:
		# ~ break
	
while True:	
	print("\nmenu\n")
	print("1- listar")
	print("2- alta")
	print("3- salir")
	opcion=int(input("Ingrese una opción: "))
	if opcion==1:
		print("listado")
	elif opcion==2:
		print("alta")
	elif opcion==3:
		break
	else:
		print("opción inexistente")	




