from operaciones import suma, resta, multiplicacion, division

otra = True

operaciones = {
    1: "suma",
    2: "resta",
    3: "multiplicacion",
    4: "division"
}
while (otra == True):
    operacion = (input("Selecciona operación a realizar (suma, resta, multiplicacion, division) => "))
    while (operacion != "suma") & (operacion != "resta") & (operacion != "multiplicacion") & (operacion != "division"):
        operacion = input("Elige una de las 4 operaciones matemáticas básicas: ")
        
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))  

    if operacion == operaciones[1]:
        print (suma(num1,num2))
    elif operacion == operaciones [2]:
        print (resta(num1,num2))
    elif operacion == operaciones[3]:
        print(multiplicacion(num1,num2))
    else:
        print(division(num1,num2))

    otra = input("¿Desea realizaar otra operación?(s/n) ")
    num1 = 0
    num2 = 0
    if otra == "n":
        break