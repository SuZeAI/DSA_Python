def main() -> None:
    t: int = int(input())
    for _ in range(t):
        s = input()
        n = len(s)
        ls = [[0] * n for i in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if i == j or j - i == 1:
                        ls[i][j] = 0
                    else: ls[i][j] = ls[i + 1][j - 1]
                else:
                    if j - i == 1:
                        ls[i][j] = 1
                    else:
                        ls[i][j] = min(ls[i + 1][j] + 1, ls[i][j - 1] + 1, ls[i + 1][j - 1] + 2)
        print(ls[0][n - 1])



main()