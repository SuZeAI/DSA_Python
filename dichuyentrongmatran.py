def main():
    t: int= int(input())
    while t > 0:
        n: int= int(input())
        ls: list= list(map(int, input().split()))
        ls.sort()
        l = 0
        r = n - 1
        cnt = 0
        while True:
            print("{} ".format(ls[r]), end="")
            cnt += 1
            if cnt == n:
                break
            print("{} ".format(ls[l]), end="")
            cnt += 1
            if cnt == n:
                break

            r -= 1
            l += 1
        print()
        t -= 1

main()