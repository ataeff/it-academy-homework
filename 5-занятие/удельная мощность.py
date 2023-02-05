# удельная мощность авто. input, numpy(float), замыкание
# LAB 2
def power(q):
    def weight(m):
        return f'УДЕЛЬНАЯ МОЩНОСТЬ АВТО: {np.array(q/m*1000, dtype=float)} kg/l.s'
    return weight

res = (power(float(input('q = '))))
print(res(float(input('m = '))))