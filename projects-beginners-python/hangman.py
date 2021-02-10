
import random

colgar = ["""
A H O R C A D O - Edicion de frutas

   +---+
   |   |
       |
       |
       |
       |
=========""", """
A H O R C A D O - Edicion de frutas

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
A H O R C A D O - Edicion de frutas

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
A H O R C A D O - Edicion de frutas

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
A H O R C A D O - Edicion de frutas

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
A H O R C A D O - Edicion de frutas

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
A H O R C A D O - Edicion de frutas

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]


def obtenerAdivinanzaAleatoria():
    palabras = ['banano', 'banana', 'mango', 'fresa', 'naranja', 'uva', 'piña', 'manzana',
             'limon', 'coco', 'sandia', 'cereza', 'papaya', 'bayas', 'melocoton', 'melon', 'ciruela', 'pera', 'Nectarina', 'pomelo',
             'Aguacate', 'Carambola', 'Chirimoya', 'Coco', 'Dátil', 'Kiwi'
'Litchi', 'Plátano' ]

    word = random.choice(palabras)
    return word


def tablero_visualizacion(colgar, cartas_perdidas, letrasCorrectas, palabraSecreta):
    print(colgar[len(cartas_perdidas)])
    print()

    print('Letras Perdidas:', end=' ')
    for letra in cartas_perdidas:
        print(letra, end=' ')
    print("\n")

    blanks = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)):  # replace blanks with correctly adivinared letras
        if palabraSecreta[i] in letrasCorrectas:
            blanks = blanks[:i] + palabraSecreta[i] + blanks[i+1:]

    for letra in blanks:  # show the secret word with spaces in between each letra
        print(letra, end=' ')
    print("\n")


def obtenerAdivinanza(yaAdivinado):
    while True:
        adivinar = input('adivina una letra: ')
        adivinar = adivinar.lower()
        if len(adivinar) != 1:
            print('introduzca una sola letra.')
        elif adivinar in yaAdivinado:
            print('Ya has adivinado esa letra. Elige de nuevo.')
        elif adivinar not in 'abcdefghijklmnopqrstuvwxyz':
            print('Por favor ingrese una LETRA.abe')
        else:
            return adivinar


def intentarDeNuevo():
    return input("\nQuieres jugar de nuevo 🤔? ").upper().startswith('y')


cartas_perdidas = ''
letrasCorrectas = ''
palabraSecreta = obtenerAdivinanzaAleatoria()
juegoHecho = False

while True:
    tablero_visualizacion(colgar, cartas_perdidas, letrasCorrectas, palabraSecreta)

    adivinar = obtenerAdivinanza(cartas_perdidas + letrasCorrectas)

    if adivinar in palabraSecreta:
        letrasCorrectas = letrasCorrectas + adivinar

        encontroTodasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontroTodasLetras = False
                break
        if encontroTodasLetras:
            print('\n¡Si! La palabra secreta es "' +
                  palabraSecreta + '"¡Usted ha ganado...🎊✨🎈🎉🎉🎉🎉🎉🎉🎉!')
            juegoHecho = True
    else:
        cartas_perdidas = cartas_perdidas + adivinar

        if len(cartas_perdidas) == len(colgar) - 1:
            tablero_visualizacion(colgar, cartas_perdidas,
                         letrasCorrectas, palabraSecreta)
            print('¡Te has quedado sin conjeturas!\Despues ' + str(len(cartas_perdidas)) + ' conjeturas perdidas y' +
                  str(len(letrasCorrectas)) + ' conjeturas correctas, la palabra era "' + palabraSecreta + '" pendejo...!!!🤮🤮🤕')
            juegoHecho = True

    if juegoHecho:
        if intentarDeNuevo():
            cartas_perdidas = ''
            letrasCorrectas = ''
            juegoHecho = False
            palabraSecreta = obtenerAdivinanzaAleatoria()
        else:
            break