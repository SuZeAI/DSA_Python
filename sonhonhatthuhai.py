def main():
    t: int = int(input())
    while t > 0:
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        nus: list= list(set(ls))
        if len(nus) > 1:
            print(nus[0],nus[1])
        else:
            print(-1)
        t -= 1
main()