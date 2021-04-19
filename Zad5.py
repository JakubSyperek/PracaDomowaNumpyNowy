import numpy as np

#5a
def wektor(x):
    w = np.arange(0, x, 2)
    print(w)
#5b
def wektor2(y):
    v = np.arange(y, 0, -2)
    print(v)
#5c
def wektor3(n):
    t = np.arange(n, 0, -1)
    return np.diag(t)



print(wektor(8))
print(wektor2(10))
print(wektor3(6))
