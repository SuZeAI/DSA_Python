mod = 1000000007
def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        lis: list = list(map(int, input().split()))
        ls: list = [0] * (k + 1)
        ls[0] = 1
        for i in range(1, k + 1):
            for j in range(n):
                if i >= lis[j]:
                    ls[i] = (ls[i] + ls[i - lis[j]]) % mod
        print(ls[k])


main()