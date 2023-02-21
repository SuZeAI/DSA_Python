from bisect import bisect_right
def main():
    t: int =  int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        ls: list = list(map(int, input().split()))
        idx = bisect_right(ls, k)
        if idx == 0:
            print(-1)
        else:
            print(idx)


main()