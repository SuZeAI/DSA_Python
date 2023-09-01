def up(n, i, u, BIT) -> None:
    while i < 2 * n + 1:
        BIT[i] += u
        i += i & -i

def qr(u, BIT) -> int:
    sum = 0
    while u > 0:
        sum += BIT[u]
        u -= u & -u
    return sum

def main() -> None:
    t: int = int(input())
    for _ in range(t):
        BIT = [0] * 40000005
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        arr = sorted(ls.copy())
        mp = dict()
        for key, val in enumerate(arr):
            mp[val] = key
        for key, val in enumerate(ls):
            ls[key] = mp[val]
        ans = 0
        for i in range(n - 1, -1, -1):
            if ls[i] == 0:
                ls[i] += 1
            ans += qr(ls[i], BIT)
            up(n, ls[i], 1, BIT)
        print(ans)

main()