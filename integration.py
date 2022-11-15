from math import sin


def intigration(lower : float, upper : float, j : list) -> list:

    dx = (upper - lower) / float(j)
    integral1 = 0.00
    i = 0

    while i < j:
        integral1+=(abs(sin((lower + i*dx)))*dx)
        i=1+i
    return integral1

lower = 0.00
upper = 3.14159
N_list = [10, 100, 100, 1000, 10000, 100000, 1000000]
results = []

for i in N_list:
    results.append(intigration(lower, upper, i))
print(results)