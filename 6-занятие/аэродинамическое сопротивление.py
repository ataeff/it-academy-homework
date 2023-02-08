"""На расход топлива в конкретном автомобиле влияет множество факторов.
Наиболее весомые – это характеристики двигателя,
трансмиссии, тип КП, конструктивные особенности и др.)
и внешние факторы сопротивления движению.
    К последним относится и аэродинамическое сопротивление (F_АС).
    Этот показатель вычисляется по формуле,которая учитывает и плотность воздуха,
и коэффициент лобового сопротивления (Сх), конкретного авто,
и лобовую площадь (S) автомобиля (площадь поперечного сечения),
и скорость движения (V). Причем именно она является наиболее существенной,
поскольку ее значение в формуле – «в квадрате».
    При выборе крупного автомобиля, да еще и с посредственными показателями
обтекаемости, следует помнить, что экономить горючее на нем можно только в ущерб
скорости движения.

# Формула:
F_АС= Cx*S*(V**2*ρ/2)
# Параметрические данные:
V - скорость (м/с)
ρ - плотность воздуха в тропосфере у земли = 1.23 кг,м**3
Cx (коэффициент АС) = F/(Q*S) (для известных марок авто выберите показатели (Сх) с сайта:
https://topruscar.ru/terminy/koeffitsient-obtekaemosti)

Q (скоростной напор) = (1.23*V**2)/2

Условие: подсчитать аэродинамическое сопротивление выбранной вами марки автомобиля
на скоростях от 25 км/ч до 250 км,ч
с шагом 10 км/ч. Создайте класс, инициализируйте конструктор, определите функциональный метод и экземпляр с выводом.
Из полученных данных составьте график кривой соотношения F_AC/V.
Определите мах F_AC c оответствующим скоростным показателем.
Альтернативно можно составить для любых, введенных пользователем скоростей.

import sympy as sp
import numpy as np
import math as mt
import matplotlib.pyplot as plt

C = sp.Symbol('Cx')
S, V, p = sp.symbols("S, V, ρ")
p= 1.23
S=в сети найдмте для вашего авто
V=[]
C= на выбор https://topruscar.ru/terminy/koeffitsient-obtekaemosti)
F_АС= (C*S)*(V**2*p/2)
print(F_АС)
"""
# Atayev Akmuhammet
# Lab 6


import matplotlib.pyplot as plt
import math as m

class Aero_drag:

    def __init__(self, model, cx, s, p=1.23):
        self.model = model
        self.cx = cx
        self.s = s
        self.p = p

    def __iter__(self):
        return range(25, 255, 10)

    def calculate(self):
        for i in self.__iter__():
            return list(map((lambda i: (self.cx * self.s * (i**2) * self.p) / 2),
                            [float(i) for i in self.__iter__()]))


    def __getitem__(self):
        return f'Aero drag of {self.model} = {self.calculate()}'

# --------------------
car = Aero_drag('BMW 518i E28', 0.39, 0.30)
print(car.__getitem__())


graph = map(lambda v: [float(i)/v for i in car.calculate()], [float(v) for v in car.__iter__()])
graph = list(graph)
print(graph)

plt.plot((graph), car.__iter__())
# plt.scatter((graph), car.__iter__())
plt.show()