def main():
    t: int = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        ls: list = list()
        for i in range(n):
            ls.append([0] + list(map(int, input().split())))
        ls = [[0] * (k + 1)] + ls
        lis2 = [[0] * (n + 1) for i in range(k + 1)]
        lis3 = lis2.copy()
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                if ls[i][j] == 1:
                    lis2[i][j] = lis2[i][j - 1] + 1
        for i in range(1, k + 1):
            for j in range(1, n + 1):
                if ls[j][i] == 1:
                    lis3[j][i] = lis3[j - 1][i] + 1
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                if ls[i][j] == 1:
                    if ls[i - 1][j - 1] >= 1:
                        if lis2[i][j - 1] >= ls[i - 1][j - 1] and lis3[i - 1][j] >= ls[i - 1][j - 1]:
                            ls[i][j] = ls[i - 1][j - 1] + 1
                if ls[i][j] > ans: ans = ls[i][j]
        print(ans)

main()