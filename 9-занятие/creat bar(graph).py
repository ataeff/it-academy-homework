"""
Создайте полезное на все случаи, для себя, интерактивное приложение по вводу данных float в поля х/у
для автоматического создания графика и баров (столбики)
Диапазоны х: 0-100, у -100-100
"""""
# Atayev Akmuhammet
# Lab 9

import matplotlib.pyplot as plt

class Graph:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def graph_plot(self):
        return plt.bar(self.x, self.y), plt.show()


b = Graph([float(x) for x in input('X: (0 - 100) = ').split()],
          [float(y) for y in input('Y: (-100 - 100) = ').split()]).graph_plot()    # input


# b = Graph(np.random.uniform(low=0, high=100, size=50),
#           np.random.uniform(low=-100, high=100, size=50)).graph_plot()              #random list
