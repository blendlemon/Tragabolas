from modulos.Jugador import *
from modulos.Slots import *
import time
import os
from random import randint

slot = Slots(["🍊","🍎","🍒","🍉","💣","🐧"])
nombre = input("Introduce tu nombre: ")
try:
    dinero = int(input("Introduce tu dinero inicial: "))
    if dinero <=0:
        raise ValueError
except ValueError:
    print("Introduce un número entero no negativo")
user = Jugador(nombre, dinero)

del nombre, dinero

while True:
    while True:
        modo_juego = input("Modo de juego manual o automático, ver saldo (m/a/v): ").lower()

        if modo_juego != "m" and modo_juego != "a" and modo_juego!="v":
            print("Introduzca una opción valida")
        else:
            break
    
    match modo_juego:

        case "a":
            slot.agame(user)
        case "m":
            slot.mgame(user)
        case "v":
            user.VerJugador()

