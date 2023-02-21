def main():
    t: int = int(input())
    while t > 0:
        n, k= map(int, input().split())
        ls: list= list(map(int, input().split()))
        ls.sort(key=lambda item: abs(k - item))
        for i in ls:
            print(i, end=" ")
        print()
        t -= 1
main()