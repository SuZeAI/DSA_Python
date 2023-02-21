def main():
    t: int = int(input())
    while t > 0:
        n, k = map(int, input().split())
        ls: list = list(map(int, input().split()))
        m = int(-1e9)
        nus = ls[:k].copy()
        for j in range(k, n):
            print(max(nus), end=" ")
            nus.pop(0)
            nus.append(ls[j])
        print(max(nus))
        t -= 1
main()