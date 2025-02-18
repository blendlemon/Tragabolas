class Jugador: 
    def __init__(self, nombre, cartera):
        self.nombre = nombre
        self.cartera = cartera
        self.mano = []
        self.wins = 0
        self.loses = 0
    
    def recarga (self):
        try:
            dinero = int(input("Dinero a recargar ---> "))
            if dinero <= 0:
                raise ValueError
        except ValueError:
            print("Debe de ser una cantidad mayor a 0")
        else:
            self.cartera += dinero
    
    def puntos(self):
        suma = 0
        for i in range(len(self.mano)):
            suma += self.mano[i][1]
        return suma