def main():
    t: int = int(input())
    while t > 0:
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        ls.sort()
        m = int(1e9 + 7)
        for i in range(n - 1):
            if m > ls[i + 1] - ls[i]:
                m = ls[i + 1] - ls[i]
        print(m)
        t -= 1
main()