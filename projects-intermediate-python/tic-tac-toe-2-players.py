import os    
import time    
    
tablero = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1    
   
########Ganador Flags----------Banderas de ganadores##########    
Ganador = 1    
dibujar = -1    
correr_juego = 0    
detenerse = 1    
###########################    
Juego = correr_juego    
Marca = 'X'    
   
#This Function dibujars Juego tablero    --------Esta función dibuja el tablero de juego
def tablero_dibujo():    
    print(" %c | %c | %c " % (tablero[1],tablero[2],tablero[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (tablero[4],tablero[5],tablero[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (tablero[7],tablero[8],tablero[9]))    
    print("   |   |   ")    
   
#This Function Checks position is empty or not--------------------------Esta posición de cheques de función está vacía o no    
def seleccionar_posicion(x):    
    if(tablero[x] == ' '):    
        return True    
    else:    
        return False 
   
#This Function Checks player has won or not ---------------Esta función comprueba que la jugadora ha ganado o no.-----#Esta función comprueba que el jugador ha ganado o no.(masculino) 
def seleccionar_ganador():    
    global Juego    
    #Horizontal Ganadorning condition    
    if(tablero[1] == tablero[2] and tablero[2] == tablero[3] and tablero[1] != ' '):    
        Juego = Ganador    
    elif(tablero[4] == tablero[5] and tablero[5] == tablero[6] and tablero[4] != ' '):    
        Juego = Ganador    
    elif(tablero[7] == tablero[8] and tablero[8] == tablero[9] and tablero[7] != ' '):    
        Juego = Ganador    
    #Vertical Ganadorning Condition    
    elif(tablero[1] == tablero[4] and tablero[4] == tablero[7] and tablero[1] != ' '):    
        Juego = Ganador    
    elif(tablero[2] == tablero[5] and tablero[5] == tablero[8] and tablero[2] != ' '):    
        Juego = Ganador    
    elif(tablero[3] == tablero[6] and tablero[6] == tablero[9] and tablero[3] != ' '):    
        Juego=Ganador    
    #Diagonal Ganadorning Condition    
    elif(tablero[1] == tablero[5] and tablero[5] == tablero[9] and tablero[5] != ' '):    
        Juego = Ganador    
    elif(tablero[3] == tablero[5] and tablero[5] == tablero[7] and tablero[5] != ' '):    
        Juego=Ganador    
    #Match Tie or dibujar Condition    
    elif(tablero[1]!=' ' and tablero[2]!=' ' and tablero[3]!=' ' and tablero[4]!=' ' and tablero[5]!=' ' and tablero[6]!=' ' and tablero[7]!=' ' and tablero[8]!=' ' and tablero[9]!=' '):    
        Juego=dibujar    
    else:            
        Juego=correr_juego    
    
print("Juego Tic-Tac-Toe diseñado por Elder Adan...🤗🤘🏽🚀")    
print("Jugador 1 [X] --- Jugador 2 [O]\n")    
print()    
print()    
print("Porfavor espere...🚀🚀")    
time.sleep(4)  #este es un tiempo de espera para que nos muestre el juego---------his is a timeout for the game to show us 
while(Juego == correr_juego):    
    os.system('cls')    #limpiara la consola es lo que hace esto y mas...------------limpiara la consola es lo que hace esto y mas .
    tablero_dibujo()    
    if(player % 2 != 0):    
        print("Oportunidad del/la jugador/a 1...😊😃")    
        Marca = 'X'    
    else:    
        print("Oportunidad del/la jugador/a 2...😊😃")    
        Marca = 'O'    
    choice = int(input("Introduzca la posición entre [1-9] donde quieres Marcar : 🤔"))    
    if(seleccionar_posicion(choice)):    
        tablero[choice] = Marca    
        player+=1    
        seleccionar_ganador()    
    
os.system('cls')    #limpiara la consola es lo que hace esto y mas...------------limpiara la consola es lo que hace esto y mas ...
tablero_dibujo()    
if(Juego==dibujar):    
    print("Juego dibujar")    
elif(Juego==Ganador):    
    player-=1    
    if(player%2!=0):    
        print("Jugador 1 Gano...🎈🎊✨🎉🎉🎉🎉")    
    else:    
        print("Jugador 2 Gano...🎈🎊✨🎉🎉🎉🎉")   