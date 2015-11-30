


from numpy import dot
from math import sqrt


def choleski(a):
    n = len(a)
    for k in range(n):
        try:
            a[k,k] = sqrt(a[k,k] - dot(a[k,0:k],a[k,0:k]))
        except ValueError:
                print('Matrix is not positive definite')
        for i in range(k+1,n):
            a[i,k] = (a[i,k] - dot(a[i,0:k],a[k,0:k]))/a[k,k]
    for k in range(1,n): a[0:k,k] = 0.0
    return a