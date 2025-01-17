from modulos.MOROSO import moroso

class Jugador:

    def __init__(self, name, wallet):

        self.name = name
        self.wallet = wallet
        self.wins = 0
        self.loses = 0

    def WalletCheck(self):

        if self.wallet <= 0:
            opcion=""
            while True:
                opcion = input("Desea seguir jugando? (Y/N): ").lower()
                if opcion =="y" or opcion=="n":
                    break

            if opcion == "y":
                while True:
                    try:
                        dinero = int(input(f"Su saldo actual es de {self.wallet}, porfavor añada más fondos: "))
                        if dinero <=0:
                            raise ValueError
                    except ValueError:
                        print("Introduzca un numero válido")
                    else:
                        self.wallet += dinero
                        break
            else:
                moroso(self.name)
        
    def VerJugador(self):
        print(f"Nombre: {self.name}")
        print(f"Saldo: {self.wallet}")
        print(f"Victorias: {self.wins}")
        print(f"Derrotas: {self.loses}")