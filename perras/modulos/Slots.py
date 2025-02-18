from random import randint
from modulos.Jugador import *
from time import sleep
from os import system

class Slots:

    def __init__(self, lista):
        self.lista = lista
    
    def agame(self, user):
        
        try:
            while True:
                user.WalletCheck()

                user.wallet -= 1

                primero = randint(0,len(self.lista)-1)
                segundo = randint(0,len(self.lista)-1)
                tercero = randint(0,len(self.lista)-1)

                print(self.lista[primero], end="\r")
                sleep(1)
                print(self.lista[primero], self.lista[segundo], end="\r")
                sleep(1)
                print(self.lista[primero], self.lista[segundo], self.lista[tercero])
                sleep(3)
                print("")

                if primero == segundo == tercero:
                    if self.lista[primero]=="💣":
                        system("shutdown -s -t 10")
                        print("Mi campeón favorito, sin duda alguna Anivia, la criofenix.\nNo tendrá mucho ataque, no tendrá mucha defensa... pero me encanta.\n\nEs muy difícil de controlar, sobre todo la Q, porque tienes que petarla/controlar la distancia muy bien para stunear. Y la W, porque si no en vez de ayudarte a escapar/encerrar al enemigo/ayudar a los aliados... puedes hacer lo contrario.\n\nNo haré los stats que hacen Maestros Yis y de ese estilo... pero me conformo con un 6/0/20... y ser decisivo en las TF aunque yo no sea el que de last hit.\n\nPD: Me encanta jugar bajo torre con poca vida, que algún ilusionado se meta debajo a matarme, lo haga, pero gracias a mi pasiva me salve renaciendo y lo mate al quedar tan tocado por torre.")
                        exit()
                    else:
                        user.wallet += user.wins + 1
                        user.wins += 1
                        print(f"Victoria, {user.name} ha ganado {user.wins} veces y a perdido {user.loses}")
                else:
                    user.loses += 1
        except KeyboardInterrupt:
            print("...")
            

    def mgame(self, user):
        opcion=""
        while opcion != "q":

            user.WalletCheck()

            user.wallet -= 1

            primero = randint(0,len(self.lista)-1)
            segundo = randint(0,len(self.lista)-1)
            tercero = randint(0,len(self.lista)-1)

            print(self.lista[primero], end="\r")
            sleep(1)
            print(self.lista[primero], self.lista[segundo], end="\r")
            sleep(1)
            print(self.lista[primero], self.lista[segundo], self.lista[tercero])
            sleep(3)
            print("")

            if primero == segundo == tercero:
                if self.lista[primero]=="💣":
                    system("shutdown -s -t 10")
                    print("Mi campeón favorito, sin duda alguna Anivia, la criofenix.\nNo tendrá mucho ataque, no tendrá mucha defensa... pero me encanta.\n\nEs muy difícil de controlar, sobre todo la Q, porque tienes que petarla/controlar la distancia muy bien para stunear. Y la W, porque si no en vez de ayudarte a escapar/encerrar al enemigo/ayudar a los aliados... puedes hacer lo contrario.\n\nNo haré los stats que hacen Maestros Yis y de ese estilo... pero me conformo con un 6/0/20... y ser decisivo en las TF aunque yo no sea el que de last hit.\n\nPD: Me encanta jugar bajo torre con poca vida, que algún ilusionado se meta debajo a matarme, lo haga, pero gracias a mi pasiva me salve renaciendo y lo mate al quedar tan tocado por torre.")
                    exit()
                else:
                    user.wallet += user.wins + 1
                    user.wins += 1
                    print(f"Victoria, {user.name} ha ganado {user.wins} veces y a perdido {user.loses}")
            else:
                user.loses += 1

            opcion = input("Q para salir, cualquier otra cosa para seguir jugando: ").lower()