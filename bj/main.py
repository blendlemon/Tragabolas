from mods.Juego import *
from mods.Jugador import *
from mods.Baraja import *
from mods.Casa import *

nico = Jugador(input("nombre---> "), int(input("Dinero---> ")))
baraja = Baraja()
baraja.Barajar()
crupier = Casa()
game = Juego()

while True:
    opcion = input("1. jugar 2. stats")

    match opcion:
        case "1":
            game.Jugar(nico,crupier,baraja)
        
        case "2":
            print(nico.cartera, "wins: ",nico.wins, "loses", nico.loses)