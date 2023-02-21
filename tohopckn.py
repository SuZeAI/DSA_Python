def main():
    ls: list = [[0 for i in range(1000)] for j in range(1000)]
    for i in range(1000):
        for j in range(i + 1):
            if i == j or j == 0:
                ls[i][j] = 1
            else:
                ls[i][j] = ls[i - 1][j - 1] + ls[i - 1][j]
                ls[i][j] %= int(1e9 + 7)

    t: int = int(input())
    while t > 0:
        n, k = map(int, input().split())
        print(ls[n][k])
        t -= 1
main()