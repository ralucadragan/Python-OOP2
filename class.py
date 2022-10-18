'''
ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria (optional)
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’

INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pt latura

ENCAPSULATION
- latura este proprietate privata
- Implementati getter, setter, deleter pt latura
- Implementati metoda ceruta de interfata (optional, doar daca ati ales sa implementati metoda abstracta aria)

- Clasa Cerc - mosteneste FormaGeometrica constructor pt raza
- raza este proprietate privata
- Implementati getter, setter, deleter pt raza
- Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte
- (optional, doar daca ati ales sa implementati metoda abstracta aria)

POLYMORPHISM
Definiti o noua metoda descrie - printati ‘Eu nu am colturi’
'''

class FormaGeometrica:

    def __init__(self):
        self.pi = 3.14

    #def aria(self):
        #aria = pi * self.raza * self.raza
        #return(aria)
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

if __name__ == '__main__':

    p1 = Patrat(5)
    print(f'Latura patratului este de {p1.get_latura()} cm.')
    p1.set_latura(7)
    print(f'Latura patratului modificat este de {p1.get_latura()} cm.')
    p1.del_latura()
    print(f'Latura patratului este acum de {p1.get_latura()} cm.')

    print('----------------------------------------')

    r1 = Cerc(10)
    print(f'Raza cercului ese de {r1.get_raza()} cm.')
    r1.set_raza(15)
    print(f'Raza cercului modificat acre {r1.get_raza()} cm.')
    r1.del_raza()
    print(f'Latura patratului este acum de {r1.get_raza()} cm.')