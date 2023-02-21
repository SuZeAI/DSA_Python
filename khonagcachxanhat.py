# ALL is OBJECT
def main():
    t: int = int(input())
    while t > 0:
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        lis = [[a, b] for b, a in enumerate(ls)]
        lis.sort(key=lambda x : x[0])
        print(lis)
        m, Min = lis.pop(0)
        ans = -1
        for a, b in lis:
            if a > m:
                ans = max(ans, b - Min)
            if Min > b:
                Min = b
                m = a
        print(ans)
        t -= 1

main()