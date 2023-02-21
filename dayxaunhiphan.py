def main():
    t: int = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        ls: list = [0] * (n + 1)
        ls[1] = 1
        ls[2] = 1
        for i in range(3, n + 1):
            ls[i] = ls[i - 2] + ls[i - 1]
        while True:
            if n == 1:
                print(0)
                break
            if n == 2:
                print(1)
                break
            if k <= ls[n - 2]:
                n -= 2
            else:
                k -= ls[n - 2]
                n -= 1


main()