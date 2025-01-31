g = lambda f : f + 4
print(g(7))

g2 = lambda a, b, c : a + b + c
print(g2(1, 2, 3))

def g3(x):
    return lambda k : k + x
g4 = g3(5)
g5 = g3(6)
print(g4(4))
print(g5(4))