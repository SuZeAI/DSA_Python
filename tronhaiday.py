def main():
    t: int= int(input())
    while t > 0:
        m, n = map(int, input().split())
        ls1: list= list(map(int, input().split()))
        ls2: list= list(map(int, input().split()))
        for i in sorted(ls1 + ls2):
            print(i, end=" ")
        print()
        t -= 1
main()