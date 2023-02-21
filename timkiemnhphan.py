def main():
    t: int = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        ls: list = list(map(int, input().split()))
        l = 0
        r = n - 1
        ans = "NO"
        while l <= r:
            mid = (l + r)//2
            if ls[mid] == k:
                ans = mid + 1
            if ls[mid] < k:
                l = mid + 1
            else:
                r = mid - 1
        print(ans)

main()