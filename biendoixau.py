def main() -> None:
    t: int = int(input())
    for _ in range(t):
        s1, s2 = input().split()
        n, m = len(s1), len(s2)
        ls = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(0, n + 1):
            for j in range(0, m + 1):
                if i == 0:
                    ls[i][j] = j
                elif j == 0:
                    ls[i][j] = i
                elif s1[i - 1] == s2[j - 1]:
                    ls[i][j] = ls[i - 1][j - 1]
                else:
                    ls[i][j] = min(ls[i - 1][j], ls[i][j - 1], ls[i - 1][j - 1]) + 1
        print(ls[n][m])
main()