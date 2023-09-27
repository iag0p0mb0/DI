def suma(num1, num2):
    return num1 + num2
def resta(num1, num2):
    return num1 - num2
def multiplicacion(num1,num2):
    return num1 * num2
def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: división por cero"

operaciones = {
    1: "suma",
    2: "resta",
    3: "multiplicacion",
    4: "división"
}

opcion = (input("Selecciona operación a realizar (suma, resta, multiplicacion, division) => "))
while (opcion != "suma") & (opcion != "resta") & (opcion != "multiplicacion") & (opcion != "division"):
    opcion = input("Elige una de las 4 operaciones matemáticas básicas: ")

if opcion == operaciones[1]:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    print (suma(num1,num2))

elif opcion == operaciones [2]:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    print (resta(num1,num2))

elif opcion == operaciones[3]:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    print(multiplicacion(num1,num2))
else:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    print(division(num1,num2))