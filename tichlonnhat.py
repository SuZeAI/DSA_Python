from bisect import bisect_right, bisect_left
def main():
    n: int = int(input())
    ls: list = list(map(int, input().split()))
    ls.sort()
    print(max(ls[0] * ls[1] * ls[n - 1], ls[n - 1] * ls[n - 2], ls[n - 1] * ls[n - 2] * ls[n - 3]))
main()