def check(li, n, k) -> bool:
    sm = 0
    l = 0
    for i in range(n):
        sm += li[i]
        while sm > k:
            sm -= li[l]
            l += 1
        if sm == k and l <= i:
            return True
    return False

def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        li: list = list(map(int, input().split()))
        if check(li, n, k):
            print("YES")
        else:
            print("NO")



main()