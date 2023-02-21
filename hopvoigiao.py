def main():
    t: int = int(input())
    while t > 0:
        m, n = map(int, input().split())
        ls1: set= set(map(int, input().split()))
        ls2: set= set(map(int, input().split()))
        for i in ls1.union(ls2):
            print(i, end=" ")
        print()
        for i in ls1.intersection(ls2):
            print(i, end=" ")
        print()
        t -= 1
main()