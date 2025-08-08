
#Suma
def suma():
        sum = num1 + num2 
        print (sum)

#Resta
def resta():
        sustraccion = num1 + num2
        print (sustraccion)

#Multiplicación
def multiplicacion():
        producto = num1 * num2
        print (producto)

#División
def division():
        div = num1 / num2
        print (div)

#Módulo
def modulo():
        residuo = num1 % num2
        print (residuo)

#Menú principal
#menú principal
i = True
while i ==True:
        num1= float(input("Ingresa el primer número de la operación: "))
        num2= float(input("Ingresa el segundo número de la operación: "))
        operador= str(input("Ingresa la el símbolo de la operción que deseas realizar(+, -, *, /, %) :"))

        if operador=="+":
                suma()

        elif operador == "-":
                resta()

        elif operador == "*":
                multiplicacion()

        elif operador == "/":
                division()

        elif operador == "%":
                modulo()

        else:
                print("\nPor favor, ingresa un operador válido")

#Repetición de ejercicio
        continuar = input ("\n¿Quieres realizar otra operación?\n Si=1 \n No=0\n ")
        if continuar == "0":
                i = False
