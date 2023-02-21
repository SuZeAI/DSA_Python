import numpy as np

MODULO = int(1e9 + 7)
def mulmatrix(ls):
    pass
def powermatrix(ls, k):
    if k == 1:
        return ls
    x: np.array = powermatrix(ls, k//2)
    if k % 2 == 0:
        return (x.dot(x)) % MODULO
    else:
        return (x.dot(x)).dot(ls) % MODULO

def main():
    t: int = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        ls: np.array = np.array([[j for j in map(int, input().split())] for i in range(n)])
        array: np.array = powermatrix(ls, k)
        print(array)
        print(np.sum(array, axis=1)[n - 1] % MODULO)


main()