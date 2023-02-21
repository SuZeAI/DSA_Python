from bisect import bisect_left
def main():
    t: int = int(input())
    while t >0:
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        print(bisect_left(ls, 1))

        t -= 1

main()