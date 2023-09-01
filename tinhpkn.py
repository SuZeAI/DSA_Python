MODULO = 1000000007
def main():
    t: int = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        mul = 1
        for i in range(n - k + 1, n + 1):
            mul *= i
            mul %= MODULO
        print(mul)

main()