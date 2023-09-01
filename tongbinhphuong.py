def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        ls: list = []
        i = 1
        while i * i <= n:
            ls.append(i * i)
            i += 1
        ans = [0] * (n + 1)
        ans[0] = 0
        for i in range(1, n + 1):
            for j in ls:
                if i >= j:
                    if ans[i] == 0:
                        ans[i] = ans[i - j] + 1
                    else:
                        ans[i] = min(ans[i], ans[i - j] + 1)
        print(ans[n])

main()