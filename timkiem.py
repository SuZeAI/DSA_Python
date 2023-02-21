def main():
    t: int = int(input())
    while t > 0:
        m,n = map(int, input().split())
        ls: list= list(map(int, input().split()))
        print(ls.index(n) + 1)
        t -= 1
main()