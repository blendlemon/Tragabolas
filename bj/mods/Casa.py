class Casa:
    def __init__(self):
        self.mano = []
    
    def puntos(self):
        suma = 0
        for i in range(len(self.mano)):
            suma += self.mano[i][1]
        return suma
