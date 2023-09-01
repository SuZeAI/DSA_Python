def main():
    ls: list = [[0 for i in range(5000)] for j in range(5000)]
    for i in range(1000):
        for j in range(i + 1):
            if i == j or j == 0:
                ls[i][j] = 1
            else:
                ls[i][j] = ls[i - 1][j - 1] + ls[i - 1][j]
                ls[i][j] %= int(1e9 + 7)
    m, k = map(int, input().split())
    i = k
    ans = 0
    while i <= 2 * m:
        ans += ls[3*m][i] - m * ls[3 * m - 3][i - 3]
        i += k
    print(ans)
main()