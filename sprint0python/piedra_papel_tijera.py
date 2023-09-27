import random

ronda = 0
jugadasGanadas = 0
jugadasPerdidas = 0

jugada = {
    1: "piedra",
    2: "papel",
    3: "tijera"
}

while(ronda != 5):
    jugadaUsuario = (input("Selecciona jugada a realizar (piedra, papel, tijera) => "))
    while (jugadaUsuario != "piedra") & (jugadaUsuario != "papel") & (jugadaUsuario != "tijera") & (jugadaUsuario != "division"):
        jugadaUsuario = input("Elige una de las jugadas establecidas: ")
    
    jugadaNPC = jugada[random.randint(1, 3)]
    

    if jugadaUsuario == jugada[1] and jugadaNPC == jugada[1] or jugadaUsuario == jugada[2] and jugadaNPC == jugada[2] or jugadaUsuario == jugada[3] and jugadaNPC == jugada[3]:
        print("Ronda empatada, " + jugadaUsuario + " empata a " + jugadaNPC)
    elif jugadaUsuario == jugada[1] and jugadaNPC == jugada[3] or jugadaUsuario == jugada[2] and jugadaNPC == jugada[1] or jugadaUsuario == jugada[3] and jugadaNPC == jugada[2]:
        print("Ronda ganada, " + jugadaUsuario + " gana a " + jugadaNPC)
        jugadasGanadas = jugadasGanadas + 1
        ronda = ronda +1
    else:
        print("Ronda perdida, " + jugadaNPC + " gana a " + jugadaUsuario)
        jugadasPerdidas = jugadasPerdidas + 1
        ronda = ronda +1


print("El resultado de tus jugadas es: ")
print("RONDAS GANADAS => " + str(jugadasGanadas))
print("RONDAS PERDIDAS => " + str(jugadasPerdidas))
if jugadasGanadas > jugadasPerdidas:
    print("¡HAS GANADO!")
else:
    print("¡HAS PERDIDO!")