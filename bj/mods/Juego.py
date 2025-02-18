from mods.Casa import *
from mods.Juego import *
from mods.Jugador import *
import random

class Juego:

    @staticmethod
    def Jugar(jugador, crupier, baraja):
        if jugador.cartera <= 0:
            jugador.recarga()
        else:
            deck = baraja.cartas.copy()
            random.shuffle(deck)
            apuesta = int(input("Cuanto quiere apostar ---> "))
            jugador.cartera -= apuesta
            turnoJugador = True
            turnoCrupier = True
            while True:
                if turnoJugador == True:
                    opcion = input("Robar o plantarse (r/p)----> ")
                if opcion.lower() == "p":
                    turnoJugador = False
                else:
                    carta = deck.pop(0)
                    jugador.mano.append(carta)
                    print(f"Has robado {carta}, tu mano ahora es {jugador.mano}")
                if turnoCrupier == True:
                    if len(crupier.mano) == 0:
                        carta = deck.pop(0)
                        crupier.mano.append(carta)
                    elif crupier.puntos() + deck[0][1] <= 21:
                        carta = deck.pop(0)
                        crupier.mano.append(carta)
                    else:
                        turnoCrupier = False
                if turnoCrupier == False and turnoJugador == False:
                    break
            
            print("Crupier: ",crupier.mano)
            print("Tu: ",jugador.mano)
            
            if (jugador.puntos() > crupier.puntos() and jugador.puntos() <= 21) or jugador.puntos() == 21:
                print(f"Has ganado {apuesta*2}")
                jugador.cartera += apuesta*2
                jugador.wins += 1
            else:
                print("Gana la casa")
                jugador.loses += 1
            
            jugador.mano = []
            crupier.mano = []
