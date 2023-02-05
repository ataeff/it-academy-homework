"""агрегирующие функции, в списке выводить min max и оставшиеся числа"""""
# --- Atayev Akmuhammet
# Lab 4.1

def agrFunc(e):
    return f'min={min(e)}, max={max(e)}, {[i for i in e if i != min(e) and i != max(e)]}'

print(agrFunc([int(i) for i in input().split()]))
