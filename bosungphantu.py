def main():
    t: int = int(input())
    while t > 0:
        n: int= int(input())
        ls: list = list(map(int, input().split()))
        ls.sort()
        cnt = 0
        for i in range(n - 1):
            if ls[i + 1] != ls[i]:
                cnt += ls[i + 1] - ls[i] - 1
        print(cnt)
        t -= 1
main()