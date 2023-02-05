"""theory of relativity"""""
# --- Atayev Akmuhammet
# Lab 3.2

import math

c = 299792458
num = []
for i in range(int(input('size of list - '))):
    num.append(int(input('number = ')))
    for m in num:
        e = m * math.pow(c,2)
    print(f'E = {e}')
