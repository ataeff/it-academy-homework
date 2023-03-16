"""
        Задание на заказ из АН РБ
     -------------------------------------------------------------------------------------------
    |   Провести расчет по формуле:  подъемной силы от угла атаки данного профиля крыла.        |
    |   В решении производится два параллельных вычисления:Сy=f*a; Y=Cy*0.5*p*V**2*S            |
    |   Динамическими данными являются угол атаки: а; плотность сухого воздуха тропосферы       |
    |   при средней температуре: p, в зависимости от высоты над уровнем моря.                   |
     -------------------------------------------------------------------------------------------
     
"""""
# Atayev Akmuhammet
# Lab 11.3

import matplotlib.pyplot as plt
import seaborn as sns


class LiftAngle:

    p = [1.2250, 1.1898, 1.1750, 1.1603, 1.1459, 1.1316, 1.1175, 1.1036, 1.0899, 1.0763, 1.0629]  # плотность воздуха на разных высотах (кг/м3)
    a = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  # углы атаки
    _f = 3.5  # (%)
    S = None
    V = None

    def __init__(self):
        LiftAngle.V = float(input("УКАЖИТЕ СКОРОСТЬ ПОЛЕТА Л/А(m/s): "))
        LiftAngle.S = float(input("УКАЖИТЕ ПЛОЩАДЬ КРЫЛА Л/А(m2): "))


    # коэффициент подъемной силы
    @classmethod
    def Calc_Cy(cls):
        cy = [int(i) * LiftAngle._f for i in LiftAngle.a]
        return cy

    # подъемная сила при разных плотностях воздуха
    @classmethod
    def Calc_Y(cls):
        # p = [1.2250, 1.1898, 1.1750, 1.1603, 1.1459, 1.1316, 1.1175, 1.1036, 1.0899, 1.0763, 1.0629]
        # cy = [-17.5, -14.0, -10.5, -7.0, -3.5, 0.0, 3.5, 7.0, 10.5, 14.0, 17.5, 21.0, 24.5, 28.0, 31.5, 35.0, 38.5, 42.0, 45.5, 49.0, 52.5, 56.0, 59.5, 63.0, 66.5, 70.0]
        res = []
        a = []
        for p in LiftAngle.p:  # p = плотность воздуха
            for cy in cls.Calc_Cy():  # cy = коэффициент подъемной силы
                # print(f'p = {p}')
                # print(f'cy = {cy}')
                a.append(round((cy * 0.5 * p * LiftAngle.V ** 2 * LiftAngle.S), 2))
            res.append(a)
            a = []
        return res

    @classmethod
    def res(cls):
        my_dict = dict(zip(obj.p, obj.Calc_Y()))
        print(f'\nПлотность воздуха (p) = {obj.p}\nКоэффициент подъемной силы (cy) = {obj.Calc_Cy()}\n')
        for key, value in my_dict.items():
            print(f'При p = {key} : Подъемная сила = {value}\n')


    @classmethod
    def graph_res(cls):
        sns.set()
        plt.plot(obj.a, obj.Calc_Cy())
        plt.scatter(obj.a, obj.Calc_Cy())
        plt.xlabel("a - угол атаки")
        plt.ylabel("Cy - коэффициент подъемной силы")
        plt.show()


if __name__ == '__main__':
    obj = LiftAngle()
    obj.res()
    obj.graph_res()
