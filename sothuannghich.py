def main():
    t: int = int(input())
    for _ in range(t):
        s = input()
        n = len(s)
        ls = [[False] * n for i in range(len(s))]
        ans = 1
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    ls[i][j] = True
                else:
                    if s[i] == s[j]:
                        if j - i == 1:
                            ls[i][j] = True
                        else:
                            ls[i][j] = ls[i + 1][j - 1]
                    if ls[i][j]:
                        ans = max(ans, j - i + 1)
        print(ans)



main()