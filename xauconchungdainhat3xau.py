def main():
    t: int = int(input())
    for _ in range(t):
        n, k, m = map(int, input().split())
        s1, s2, s3 = input().split()
        ls = [[[0 for i in range(m + 1)] for j in range(k + 1)]] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for h in range(1, m + 1):
                    if s1[i - 1] == s2[j - 1] == s3[h - 1]:
                        ls[i][j][h] = ls[i - 1][j - 1][h - 1] + 1
                    else:
                        ls[i][j][h] = max(ls[i - 1][j][h], ls[i][j - 1][h], ls[i][j][h - 1])
        print(ls[n][k][m])


main()