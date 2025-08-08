##Programa para generation Mex
##Calculadora sencilla con dos numeros como inputs

##Definicion de variables
resultado=0 ##Inicializacion de resultado en 0


##Definicion de funciones para cada operador
def sumar(a,b):
     resultado = a+b
     return resultado
def restar(a,b):
     resultado = a-b
     return resultado
def multiplicar(a,b):
     resultado = a*b
     return resultado
def dividir(a,b):
     if b<=0:
         print("No puedes divir con cero negativo")
     resultado = a/b
     return resultado


def calculadora():
    power = 1   ##Inicializacion del sentinela power
    ##Bucle While con sentinela power para interar el menu de operaciones hasta salir 
    while power == 1:
        print("*********Escribe el numero de la operacion a realizar********* \n"
        "   Suma: 1 \n"
        "   Resta: 2 \n"
        "   Multiplicacion: 3 \n"
        "   Division: 4 \n"
        "   Para salir: 5")
        ##variable para elegir el operador
        operador = int(input("La operacion a realizar: \n"))

        ##Condicionales para entrar al operador
        if operador == 5:
            print("Bye")
            power = 0
        elif operador in [1,2,3,4]:
            numero1 = float(input("Dame el primer numero a operar: \n"))
            numero2 = float(input("Dame el segundo numero a operar: "))
            if operador == 1:
                print( "---------- El resultado es: ", sumar(numero1, numero2), "----------\n")
            elif operador == 2:
                print( "---------- El resultado es: ", restar(numero1, numero2), "----------\n")
            elif operador == 3:
                ##resultado = numero1 * numero2
                print( "---------- El resultado es: ", multiplicar(numero1, numero2), "----------\n")
            elif operador == 4:
                print( "---------- El resultado es: ", dividir(numero1, numero2), "----------\n")
        else:
                print("-------eliga un operador correcto--------")

def isItEven(int):
    ChequeoPar = bool
    if numero % 2==0:
          ChequeoPar = True
          print("Tu numero es par: ", ChequeoPar)
    elif numero % 3 == 0:
         ChequeoPar = False
         print("Tu numero es inpar", ChequeoPar)

def isitaninteger(num):
    ChecarEntero = bool
    if type(num) == int:
        ChecarEntero = True
        print("El numero es entero", ChecarEntero)
    else:
        ChecarEntero = False
        print("El numero es entero", ChecarEntero)

def addmultiplenumbers():
    sumaNumeros=[]
    cantidad = int(input("Cuantos numeros quieres sumar?"))

    for i in range(cantidad):
        numero = float(input("Ingrese el numero: "))
        sumaNumeros.append(numero)

    resultado= sum(sumaNumeros)
    print(f"Lista de numeros {sumaNumeros}")
    print(f"El resulatdo es:  {resultado}")

def multiplymultiplenumbers():
    multiNumeros=[]
    cantidad = int(input("Cuantos numeros quieres multiplcar?"))

    for i in range(cantidad):
        numero = float(input("ingrese el numero: "))
        multiNumeros.append(numero)
        
    ##multiplicamos los elemntos de la lista
    resultados = []
    ##REcorreomos los elemntos de la lista hasta la penultima posicion
    for i in range(len(multiNumeros) -1):
        ##Multiplicamos la posicion actual por la siguiente en producto
        producto = multiNumeros[i] * multiNumeros[i + 1]
        ##Guardamos los resultados en la lista resulatdos gracias a producto
        resultados.append(producto)
        print(f"Resultados de la multipliacion: {resultados}")



###Ipresion en consola para dar la bienvenida
print("********* Bienvenido a mi Calculadora en Py *********\n")
print("Escribe 'Calculadora' para entrar a la calculadora\n")
print("Escribe 'Par' para checar si un numero es par o inpar\n")

menu= input("Tu opcion: ").upper()

mainPower = 1

while mainPower==1 :
    if menu == "CALCULADORA":
        calculadora()
    elif menu == "PAR":
        numero = int(input("Escribe el numero para revisar si es para: "))
        isItEven(numero)
    elif menu == "ENTERO":
        entero = int(input("Escribe tu tu numero para verificar si es entero: "))
    elif menu == "SUMA LISTA":
        addmultiplenumbers()
    elif menu == "MULTI LISTA":
        multiplymultiplenumbers()
    else:
        print("Good Bye")