import math
class Figura:
    def __init__(self, x, y, visible):
        self.x = x
        self.y = y
        self.visible = visible

    def getX(self):
      return self.x

    def setX(self,x):
      self.x=x 
    
    def getY(self):
      return self.y

    def setY(self,y):
      self.y=y 

    def getVisible(self):
      return self.visible

    def setVisible(self,visible):
      self.y=visible


class Rectangulo(Figura):
    def __init__(self, x, y, visible, alto, ancho):
        super().__init__(x, y, visible)
        self.alto = alto
        self.ancho = ancho

    def calcularArea(self):
        return self.alto * self.ancho

    def ocultar(self):
        super().ocultar()

    def mostrar(self):
        super().mostrar()

    def mover(self, x, y):
        super().mover(x, y)
    

class Circulo(Figura):
    def __init__(self, x, y, visible, radio):
        super().__init__(x, y, visible)
        self.radio = radio

    def calcularArea(self):
        return math.pi * (self.radio ** 2)

    def ocultar(self):
        super().ocultar()

    def mostrar(self):
        super().mostrar()

    def mover(self, x, y):
        super().mover(x, y)