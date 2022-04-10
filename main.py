import math


class Vector:
    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z

    def plus(self, object):
        plus = self.X + object.X, self.Y + object.Y, self.Z + object.Z
        return plus

    def minus(self, object):
        minus = self.X - object.X, self.Y - object.Y, self.Z - object.Z
        return minus

    def scal(self, object):
        scal = self.X * object.X + self.Y * object.Y + self.Z * object.Z
        return scal

    def lenght(self):
        lenght = math.sqrt((self.X ** 2) + (self.Y ** 2) + (self.Z ** 2))
        return lenght

    def cos(self):
        cos = V1.scal(V2) / (V1.lenght() * V2.lenght())
        return cos


while True:
    try:
        x, y, z = map(int, input('Введите через пробел три координаты первого вектора: ').split())
        break
    except ValueError:
        print('Ошибка! Необходимо ввести три значения через пробел!\n')

while True:
    try:
        x1, y1, z1 = map(int, input('Введите через пробел три координаты второго вектора: ').split())
        break
    except ValueError:
        print('Ошибка! Необходимо ввести три значения через пробел!\n')

V1 = Vector(x, y, z)
V2 = Vector(x1, y1, z1)

menu = ''
while menu != 0:
    while True:
        try:
            print('Вы в меню.')
            print('1: Сложение векторов')
            print('2: Вычитание векторов')
            print('3: Скалярное произведение векторов')
            print('4.1: Длина первого вектора')
            print('4.2: Длина второго вектора')
            print('5: Косинус угла между векторами')
            menu = float(input('\nВведите цифру действия: '))
            break

        except ValueError:
            print('\nВведите одну из предложенных цифр:')

    if menu == 0:
        print('Завершение программы...')

    if menu == 1:
        print('Ответ:', V1.plus(V2), '\n')

    if menu == 2:
        print('Ответ:', V1.minus(V2), '\n')

    if menu == 3:
        print('Ответ:', V1.scal(V2), '\n')

    if menu == 4.1:
        print('Ответ:', V1.lenght(), '\n')

    if menu == 4.2:
        print('Ответ:', V2.lenght(), '\n')

    if menu == 5:
        print('Ответ:', V1.cos(), '\n')

    else:
        print('\nВведите одну из предложенных цифр:')
