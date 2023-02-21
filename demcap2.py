from bisect import bisect_left
def main():
    t: int = int(input())
    while t > 0:
        n, k = map(int, input().split())
        ls: list = list(map(int, input().split()))
        ls.sort()
        cnt = 0
        for i in range(n):
            tmp = bisect_left(ls, k + ls[i], i + 1, n)
            cnt += tmp - i - 1
        print(cnt)
        t -= 1
main()