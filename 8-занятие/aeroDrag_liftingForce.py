""""
X = Cx*S*(V**2*ρ/2)         -> аэродинамическое сопротивление
Y = Cy*S*(V**2*ρ/2)         -> подъемная сила

Cx = 0.01,0.02...0.1
Cy = 0.1,0.2...1
S = 0.47 m^2
V = 27 m/c
p = 1.23

Объявлять 2 статик метода (с мап, лямбда итерацией с генерацией на графике matplot) в классе
Данные идут как атрибуты класса
Ордината под Cy, абсцисса под Cx
-----------------------
Продолжение
Получили график Y/X. Теперь создадим дочерный класс, берущий аргументы из первого
и сделаем обратку для получения Cy/Cx
"""""
# Atayev Akmuhammet
### - 7 - ###

import matplotlib.pyplot as plt
import numpy as np

class Myclass:

    S = 0.47
    V = 27
    p = 1.23

    @staticmethod
    def aero_drag():
        return list(map(lambda Cx: (Cx * Myclass.S * (Myclass.V ** 2) * Myclass.p) / 2,
                                  [float(Cx) for Cx in np.arange(0.01, 0.11, 0.01)]))

    @staticmethod
    def lift_force():
        return list(map(lambda Cy: (Cy * Myclass.S * (Myclass.V ** 2) * Myclass.p) / 2,
                                  [float(Cy) for Cy in np.arange(0.1, 1.1, 0.1)]))

    @classmethod
    def graph(cls):
        return plt.stem((Myclass.aero_drag()), (Myclass.lift_force())), \
               plt.xlabel('Aero_drag'), plt.ylabel('Lift_force'), plt.show()


aero = Myclass()
print(aero.aero_drag())
print(aero.lift_force())
aero.graph()