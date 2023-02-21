def main():
    t: int= int(input())
    while t > 0:
        n, x = map(int, input().split())
        ls: list = list(map(int, input().split()))
        idx = ls.count(x)
        if idx:
            print(idx)
        else:
            print(-1)
        t -= 1
main()