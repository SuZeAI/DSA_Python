def main():
    t = int(input())
    while t > 0:
        n, k = map(int, input().split())
        ls: list= list(map(int, input().split()))
        ls.sort()
        j: int= 0
        for i in reversed(ls):
            print(i, end=" ")
            j += 1
            if j == k:
                break
        print()
        t -= 1

main()