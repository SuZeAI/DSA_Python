def main():
    t: int= int(input())
    while t > 0:
        n, k = map(int, input().split())
        ls: list= list(map(int, input().split()))
        nus = ls.copy()
        cnt = 0
        for i in nus:
            ls.pop(0)
            cnt += ls.count(k - i)
        print(cnt)
        t -= 1

main()