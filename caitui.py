def main():
    t: int = int(input())
    for _ in range(t):
        n, v = map(int, input().split())
        a = [0] + list(map(int, input().split()))
        c = [0] + list(map(int, input().split()))
        arr = [[0] * (v + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, v + 1):
                if a[i] <= j:
                    arr[i][j] = max(arr[i - 1][j - a[i]] + c[i], arr[i - 1][j])
                else:
                    arr[i][j] = arr[i - 1][j]
        print(arr[n][v])

main()