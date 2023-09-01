def main() -> None:
    s, n = map(int, input().split())
    ls = list()
    for i in range(n):
        tmp = int(input())
        ls.append(tmp)
    ls = [0] + ls
    arr = [[0] * (s + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if ls[i] <= j:
                arr[i][j] = max(arr[i - 1][j - ls[i]] + ls[i], arr[i - 1][j])
            else:
                arr[i][j] = arr[i - 1][j]
    print(arr[n][s])

main()