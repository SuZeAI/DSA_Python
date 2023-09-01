def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        ls: list = [0] + list(map(int, input().split()))
        arr = [0] * (n + 1)
        arr[1] = ls[1]
        arr[2] = max(ls[1], ls[2])
        for i in range(3, n + 1):
            arr[i] = max(arr[i - 2] + ls[i], arr[i - 1])
        print(arr[n])

main()