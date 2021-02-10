import random
# library that we use in order to choose ------biblioteca que usamos para elegir
# on random words from a list of words--------de palabras aleatorias de una lista de palabras
name = input("cual es tu nombre? ")
# Here the user is asked to enter the name first---------Aquí se le pide a la usuario que ingrese el nombre primero.

print("Buena suerte! ", name)

# word yo choice-----palabra a elegir
words = ['computadora', 'programar', 
		'nombre', 'empezar',
		'agua', 'celular', 'popo', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '10'] 

# Function will choose one random-La función elegirá una al azar
# word from this list of words---# palabra de esta lista de palabras
word = random.choice(words)


print("adivina l@s personajes")

guesses = ''

# any number of turns can be used here---------- Aquí se puede utilizar cualquier número de vueltas
turns = 12


while turns > 0:
	
	# counts the number of times a user fails---------cuenta la cantidad de veces que falla un usuario
	failed = 0
	
	# all characters from the input----------todos los caracteres de la entrada
	# word taking one at a time.---------palabra tomando una a la vez.
	for char in word: 
		
		# comparing that character with-----comparando ese personaje con
		# the character in guesses---------el personaje en conjeturas
		if char in guesses: 
			print(char)
			
		else: 
			print("NO ES CORRECTO")
			
			# for every failure 1 will be
			# incremented in failure
			failed += 1
			

	if failed == 0:
		# user will win the game if failure is 0---------usuario ganará el juego si falla 0
		# and 'You Win' will be given as output-------y 'You Win' se darán como salida
		print("ganastes...!!!🎉🎉") 
		
		# this print the correct word-----------ESTA PARALABRA ES CORRECTA
		print("La palabra es: ", word) 
		break
	
	# if user has input the wrong alphabet then------si el usuario ha introducido el alfabeto incorrecto,
	# it will ask user to enter another alphabet-------------# le pedirá al usuario que ingrese otro alfabeto
	guess = input("adivina un personaje:")
	
	# every input character will be stored in guesses 
	guesses += guess 
	
	# check input with the character in word
	if guess not in word:
		
		turns -= 1
		
		# if the character doesn’t match the word-----si el carácter no coincide con la palabra
		# then “Wrong” will be given as output --------entonces se dará "Incorrecto" como salida
		print("incorrecto")
		
		# this will print the number of----# esto imprimirá el número de
		# turns left for the user---------# vueltas a la izquierda para el usuario
		print("tu tienes", + turns, 'mas oportunidades')
		
		# SI EL CONTADOR LLEGO A 0 EL RESULTADO SERA
		if turns == 0:
			print("PERDISTES...!!!😣😞")
