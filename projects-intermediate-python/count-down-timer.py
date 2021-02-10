# import the time module -----------importar el módulo de tiempo
import time 

# define the countdown func.---definir la función de cuenta regresiva.
def cuenta_regresiva(t): 
	
	while t: 
		mins, secs = divmod(t, 60) #El método divmod () toma dos números y devuelve un par de números (una tupla) que consta de su cociente y resto.
		timer = '{:02d}:{:02d}'.format(mins, secs) 
		print(timer, end="\r") 
		time.sleep(1)  #El método de tiempo de Python sleep () suspende la ejecución durante el número de segundos especificado. El argumento puede ser un número de coma flotante para indicar un tiempo de reposo más preciso.
		t -= 1
	
	print('¡¡Fuego en el hoyo!!') 


# input time in seconds ----------tiempo de entrada en segundos
t = input("ingrese el tiempo en segundos: ") 

# function call 
cuenta_regresiva(int(t)) 


# Paso 1: Importe el módulo de TIEMPO.
# Paso 2: luego pida al usuario que ingrese la duración de la cuenta regresiva en segundos.
# Paso 3: Este valor se envía como un parámetro 't' a la función definida por el usuario cuenta_regresiva () . Cualquier variable que se lea usando la función de entrada es una cadena. Entonces, convierta este parámetro a 'int' ya que es de tipo cadena.
# Paso 4: En esta función, se ejecuta un ciclo while hasta que el tiempo se vuelve 0.
# Paso 5: use divmod () para calcular la cantidad de minutos y segundos. Puedes leer más sobre esto aquí.
# Paso 6: Ahora imprima los minutos y segundos en la pantalla usando el formato de tiempo variable .
# Paso 7: Usando end = '\ r' forzamos al cursor a regresar al inicio de la pantalla (retorno de carro) para que la siguiente línea impresa sobrescriba la anterior.
# Paso 8: El time.sleep () se utiliza para hacer que la espera de código para uno sec.
# Paso 9: Ahora disminuya el tiempo para que el ciclo while pueda converger.
# Paso 10: Después de completar el ciclo, imprimiremos "Fuego en el hoyo" para indicar el final de la cuenta regresiva.