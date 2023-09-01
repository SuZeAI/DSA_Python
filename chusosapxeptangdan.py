def main() -> None:
    mod = 1000000007
    t:int = int(input())
    for _ in range(t):
        n: int = int(input())
        ls: list = [1] * 10
        ls[0] = 0
        ans = [0] * (n + 1)
        ans[1] = 10
        for i in range(2, n + 1):
            sm = 0
            for j in range(1,10):
                sm += ls[j]
                sm %= mod
                ls[j] = sm 
            ans[i] = (sum(ls) % mod + ans[i - 1] % mod) % mod
        print(ans[n])
main()