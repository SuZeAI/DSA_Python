def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        arr: list =[0] + list(map(int, input().split()))
        ls: list = [0] * 1000005
        ls[1] = arr[1]
        ls[2] = max(arr[1], arr[2])
        for i in range(3, n + 1):
            ls[i] = max(ls[i - 2] + arr[i], ls[i - 1])
        print(ls[n])


main()