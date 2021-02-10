# function to ask play again or not---# función para pedir jugar de nuevo o no
def juega_nuevamente():
  print("\n¿Quieres jugar de nuevo? (y or n)")
  
  # convert the player's input to lower_case-------------# convierte la entrada del jugador a minúsculas
  responder = input(">").lower()

  if "y" in responder:
    # if player typed "yes" or "y" start the game from the beginning-----# si el jugador escribió "sí" o "y", comience el juego desde el principio
    start()
  else:
    # if user types anything besides "yes" or "y", exit() the program----# si el usuario escribe algo además de "sí" o "y", salga () del programa
    exit()



# juego_perdido function accepts an argument called "razon"--------# La función juego_perdido acepta un argumento llamado "razon"
def juego_perdido(razon):
  # print the "razon" in a new line (\n)-----# imprime la "razon" en una nueva línea (\ n)
  print("\n" + razon)
  print("juego perdido!")
  # ask player to play again or not by activating juega_nuevamente() function------# pedirle al jugador que vuelva a jugar o no activando la función juega_nuevamente ()
  juega_nuevamente()



# diamond room----
def habitacion_diamantes():
  # some prompts------algunas entradas
  print("\n")
  print("¡Y también hay una puerta!")
  print("¿Qué harías? (1 or 2)")
  print("1). Toma algunos diamantes y atraviesa la puerta.")
  print("2). Solo atraviesa la puerta.")

  # take input()-----tomar entrada
  responder = input(">")
  
  if responder == "1":
    # the player is dead, call juego_perdido() function with the "razon"----------# el jugador está muerto, llama a la función juego_perdido () con el "razon"
    juego_perdido("¡Eran diamantes malditos! En el momento en que lo tocaste, el edificio se derrumbó y tú mueres. ⚰🤕")
  elif responder == "2":
    # the player won the game---------# El jugador ganó el juego(masculino)  # La jugadora ganó el juego(masculino)
    print("\n¡Bien, eres un hombre honesto! ¡Felicidades por ganar el juego!...🎈🎉✨")
    # activa juega_nuevamente() funcion
    juega_nuevamente()
  else:
    # call juego_perdido() with "razon"
    juego_perdido("Ve y aprende a escribir un número....PENDEJO 🤮")



# monster room
def habitacion_monstruo():
  # some prompts
  # '\n' is to print the line in a new line
  print("\n¡Ahora entraste en la habitación de un monstruo!")
  print("El monstruo está durmiendo. \n Detrás del monstruo, hay otra puerta. ¿Qué harías? (1 o 2)")
  print("1). Atraviesa la puerta en silencio.")
  print("2). ¡Mata al monstruo y muestra tu coraje!")

  # take input()
  responder = input(">")

  if responder == "1":
    # lead him to the habitacion_diamantes()----llevarlo a habitacion_diamantes ()
    habitacion_diamantes()
  elif responder == "2":
    # the player is dead, call juego_perdido() with "razon"
    juego_perdido("El monstruo tenía hambre, te comió.")
  else:
    # juego_perdido() with "razon"------------juego_perdido() con "razon"
    juego_perdido("Ve y aprende a escribir un número....PENDEJO 🤮")



# bear room----habitacion de oso
def habitacion_oso():
  # give some prompts-----dar algunas indicaciones
  # '\n' is to print the line in a new line-----  # '\ n' es imprimir la línea en una nueva línea
  print("\n aqui hay un oso")
  print("Detras del oso hay otra puerta🧸🐻🚪🚪")
  print("¡El oso está comiendo miel sabrosa!")
  print("¿Qué harías? (1 o 2)")
  print("1). Toma la miel.🍯🍯")
  print("2). Burlarse del oso. 🧸🐻")

  # take input()
  responder = input(">")
  
  if responder == "1":
    # the player is dead!
    juego_perdido("El oso te mato...💀⚰")
  elif responder == "2":
    # lead him to the habitacion_diamantes()---llevarlo a habitacion_diamantes ()
    print("\nTu buen rato, el oso se apartó de la puerta. ¡Puedes revisarlo ahora!")
    habitacion_diamantes()
  else:
    # else call juego_perdido() function with the "razon" argument-----# else llama a la función juego_perdido () con el argumento "razon"
    juego_perdido("¿No sabes cómo escribir un número....TONTO 🤮?")



def start():
  # give some prompts.-----dar algunas indicaciones.
  print("\nEstás de pie en una habitación oscura.")
  print("Hay una puerta a tu izquierda y derecha, ¿cuál escoges? (l or r)")
  
  # convert the player's input() to lower_case----------convierte la entrada del jugador () a minúsculas
  responder = input(">").lower()

  if "l" in responder:
    # if player typed "left" or "l" lead him to habitacion_oso()----------si el jugador escribió "izquierda" o "l", llévelo a habitacion_oso ()
    habitacion_oso()
  elif "r" in responder:
    # else if player typed "right" or "r" lead him to habitacion_monstruo()----de lo contrario, si el jugador escribió "derecha" o "r", llévelo a habitacion_monstruo ()
    habitacion_monstruo()
  else:
    # else call juego_perdido() function with the "razon" argument-------si no, llama a la función juego_perdido () con el argumento "razón"
    juego_perdido("¿No sabes cómo escribir algo correctamente??")


# start the game-----------inicie el juego
start()