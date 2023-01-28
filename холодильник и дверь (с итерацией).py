#------------ the fridge and the door with iterables
import random

def fridge(a, b):
    fridge_size = []
    for i in range(int(input('how many fridges = '))):
        x = random.randint(1, 50)
        y = random.randint(1, 50)
        h = random.randint(50, 100)
        fridge_size.append(x * y * h)
    print(f'fridges = {fridge_size}')
    door_size = a * b
    return [elements for elements in fridge_size if elements < door_size]

print(fridge(int(input('door_side_1 = ')), int(input('door_side_2 = '))))
