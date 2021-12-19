class Carro():
    aceleracion = 0
    def __init__(self,color, puertas):
        self.color = color
        self.puertas = puertas

    def acelerar(self,n=100, x=4):
        ''' por defecto n = 100'''
        self.aceleracion = n - x

    def frenar(self):
                                                                      self.aceleracion = 0

    def hora(self):
        self.frenar()
        return '2 pm'

if __name__ == '__main__':
    r = Carro.acelerar()
    print(r)