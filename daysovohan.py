MODULO = int(1e9 + 7)

def mulmatrix(mt1: list[list[int]], mt2: list[list[int]]) -> list[list[int]]:
    mt = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                tmp = (mt1[i][k] * mt2[k][j]) % MODULO
                mt[i][j] += tmp
    return mt


def fibon(mt: list[list[int]], n) -> list[list[int]] | int:
    if n == 1:
        return mt
    mtr = fibon(mt, n//2)
    if n % 2 == 0:
        return mulmatrix(mtr, mtr)
    else:
        return mulmatrix(mulmatrix(mtr, mtr), [[1, 1], [1, 0]])


def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        if n == 0:
            print(0)
        elif n == 1:
            print(1)
        else:
            print(fibon([[1, 1], [1, 0]], n)[1][0])


main()
