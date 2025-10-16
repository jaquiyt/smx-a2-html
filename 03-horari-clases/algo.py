print("Bien venido a la calculadora, elige numeros y la operacion que quieras realizar: ")
repetir = True
while repetir == True:
    num1 = int(input("Pon el primer numero: "))
    opera = int(input("Elije operacion (1-> +, 2-> -, 3-> x, 4-> /, 5-> ^)  "))
    num2 = int(input("Pon el segundo numero: "))

    if opera == 1:
        result = num1 + num2
    elif opera == 2:
        result = num1 - num2
    elif opera == 3:
        result = num1 * num2
    elif opera == 4:
        result = num1 / num2
    #la potencia no funciona+ bien
    elif opera == 5:
            result= num1 ** num2
    else:
        print("No has elegido una opcion valida!")

    print(result)
    pregunta = int(input("Introduce '1' para seguir calculando o '2' para detener el programa: "))
    if pregunta == 2:
        repetir = False
    else:
        repetir = True
        print("Calculadora detenida")