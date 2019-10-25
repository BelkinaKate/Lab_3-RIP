from lab_python_oop import Rectangle
from lab_python_oop import Property


class Square(Rectangle):
    def __init__(self, side, color):
        self.__side = side
        self.__c = Property.Colour()
        self.__c.col = color
        self.__name = 'Square'

    def square(self):
        return self.__side ** 2

    def __repr__(self):
        return 'Parameters of figure: \n \
        Side = {} \n \
        Colour = {} \n \
        Square = {}'.format(self.__side, self.__c, self.square())
