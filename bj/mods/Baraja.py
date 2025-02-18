class Baraja:

    def __init__(self):
        self.cartas = []
    
    def Barajar(self):
        palos =["corazones", "treboles", "picas", "rombos"]
        for i in range(4):
            for j in range(1, 12):
                carta = [palos[i], j]
                self.cartas.append(carta)
            for x in range(4):
                carta = [palos[i], 10]
                self.cartas.append(carta)