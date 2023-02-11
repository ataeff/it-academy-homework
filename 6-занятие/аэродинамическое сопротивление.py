"""Подсчитать аэродинамическое сопротивление выбранной вами марки автомобиля
на скоростях от 25 км/ч до 250 км,ч с шагом 10 км/ч. Создайте класс, инициализируйте конструктор,
определите функциональный метод и экземпляр с выводом.
Из полученных данных составьте график кривой соотношения F_AC/V.
# Формула:
F_АС= Cx*S*(V**2*ρ/2)
V - скорость (м/с)
ρ - плотность воздуха в тропосфере у земли = 1.23 кг,м**3
Cx (коэффициент АС)
"""
# Atayev Akmuhammet
# Lab 6

import matplotlib.pyplot as plt
import numpy as np

class Aero_drag:

    def __init__(self, model, cx, s, p=1.23):
        self.model = model
        self.cx = cx
        self.s = s
        self.p = p

    # метод итерация для скорости: (25-250 по 10) км/ч => м/с
    def __iter__(self):
        return list(map(float, [float(i) for i in np.arange(6.94, 70.83, 2.77)]))

    # МЕТОД РАСЧЕТА F_AC В СКОРОСТЯХ: (25-250 по 10) км/ч
    def F_AC(self):
        return list(map(lambda i: (self.cx * self.s * (i ** 2) * self.p) / 2,
                        [float(i) for i in self.__iter__()]))

    # результат
    def get_F_AC(self):
        return f'Aero drag of {self.model} = {self.F_AC()}'

    # МЕТОД РАСЧЕТА F_AC/V: (25-250 по 10) км/ч
    def divide_to_speed(self):
        return list(map(lambda x, y: x / y, self.F_AC(), self.__iter__()))

    # результат F_AC/V
    def get_divide_to_speed(self):
        return f'F_AC / V = {self.divide_to_speed()}'

# --------------------
car = Aero_drag('BMW 518i E28', 0.39, 0.30)     #atributes = model, cx, s

# --------- ГРАФИК F_AC В СКОРОСТЯХ: (25-250 по 10) км/ч
plt.title('F_AC в скоростях: (25-250 по 10) км/ч')
plt.ylabel('V м/с')
plt.stem((car.__iter__()), (car.F_AC()))
plt.show()


# ---------- ГРАФИК F_AC/V В СКОРОСТЯХ: (25-250 по 10) км/ч
plt.title('F_AC / V в скоростях: (25-250 по 10) км/ч')
plt.ylabel('V м/с')
plt.stem((car.__iter__()), (car.divide_to_speed()))
plt.show()
