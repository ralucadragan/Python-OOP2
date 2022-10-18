
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):

    def __init__(self):
        self.pi = 3.14

    @abstractmethod
    def aria(self):
        pass
    def descriere(self):
        print('Cel mai probabil am colturi!')

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        FormaGeometrica.__init__(self)
        self.__latura = latura

    def get_latura(self):
        return self.__latura
    def set_latura(self, new_latura):
        self.__latura = new_latura
    def del_latura(self):
        print(f'Am sters latura patratului.')
        self.__latura = None
    def aria(self):
        aria = self.__latura**2
        return aria

class Cerc(FormaGeometrica):
    def __init__(self, raza):
        FormaGeometrica.__init__(self,)
        self.__raza = raza

    def get_raza(self):
        return self.__raza
    def set_raza(self, new_raza):
        self.__raza = new_raza
    def del_raza(self):
        print(f'Am sters latura cercului.')
        self.__raza = None
    def aria(self):
        aria = self.pi * self.__raza ** 2
        return aria

if __name__ == '__main__':

    p1 = Patrat(5)
    print(f'Latura patratului este de {p1.get_latura()} cm.')
    p1.aria()
    print(f'Aria patratului este de {p1.aria()} cmp.')
    p1.set_latura(7)
    print(f'Latura patratului modificat este de {p1.get_latura()} cm.')
    p1.aria()
    print(f'Aria patratului este de {p1.aria()} cmp.')
    p1.del_latura()
    print(f'Latura patratului este acum de {p1.get_latura()} cm.')

    print('----------------------------------------')

    r1 = Cerc(10)
    print(f'Raza cercului ese de {r1.get_raza()} cm.')
    r1.aria()
    print(f'Aria cercului este de {r1.aria()} cmp.')
    r1.set_raza(15)
    print(f'Raza cercului modificat are {r1.get_raza()} cm.')
    r1.aria()
    print(f'Aria cercului este de {r1.aria()} cmp.')
    r1.del_raza()
    print(f'Latura patratului este acum de {r1.get_raza()} cm.')

    print('----------------------------------------')

