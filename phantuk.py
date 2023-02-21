def main():
    t: int = int(input())
    for _ in range(t):
        n, k, m = map(int, input().split())
        ls1: list = list(map(int, input().split()))
        ls2: list = list(map(int, input().split()))
        ls = ls1 + ls2
        ls.sort()
        print(ls[m- 1])
main()