# -- Создайте пользовательский ввод списка в диапазоне до 10,
# -- преобразующего данные в float и выводящего в результате массив данных, уменьшенных в 5 раз
# -- * вложенный и фабричный *
# LAB 1
import numpy as np
def list_func():
    m = [input(f'{i} = ') for i in range(1, 11)]
    def arr_func(n):
        return np.array(m, 'f') - n
    return arr_func

x = list_func()
print(x(5))


# --без функции
# print(np.array([input(f'{i} = ') for i in range(1, 11)], 'f'))