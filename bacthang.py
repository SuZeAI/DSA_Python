MODULO = 1000000007


def power(n):
    if n == 0:
        return 1
    x = power(n//2)
    if n & 1:
        return (x * x * 2) % MODULO
    else:
        return (x * x) % MODULO


def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        ls = [0] * (n + 1)
        for i in range(1, min(k, n) + 1):
            ls[i] = power(i - 1)
        for i in range(k + 1, n + 1):
            ls[i] = 0
            for j in range(1, k + 1):
                ls[i] += ls[i - j]
        print(ls[n])


main()