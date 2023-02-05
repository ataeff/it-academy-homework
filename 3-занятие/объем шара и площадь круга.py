"""объем шара и площадь круга"""""
# --- Atayev Akmuhammet
# Lab 3.1

import math as m

def f(r):
    choice = int(input('S - 1 / V - 0: '))
    return m.pi * pow(r, 2) if choice == 1 else (3/4) * m.pi * pow(r, 3)

print(f(int(input('r = '))))
