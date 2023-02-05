"""сила лобового сопротивления F = V^2. несколько поль.ввод через пробел (напр: 50, 80, 100...)"""""
# --- Atayev Akmuhammet
# Lab 4.2

def drag_force(v):
    return list(map(lambda x: x*x, [int(i) for i in v]))

print(drag_force(input('v: ').split(' ')))
