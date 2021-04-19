import numpy as np

def potega(n,k):
    x = np.logspace(1, k, num=k, base=n)
    print(x)

print(potega(3,6))

