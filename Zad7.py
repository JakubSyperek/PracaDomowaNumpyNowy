import numpy as np

#def wektor(n):
#    a = np.arange(n*n).reshape(n,n)
#    print(a)


#print(wektor(3))

def macierz(n):
    a = np.zeros((n, n), int)
    h = np.fill_diagonal(a, 2)
    print(a)
    mat_diag_k = np.diag([a for a in range(5)], -1)
    print(mat_diag_k)

print(macierz(3))

