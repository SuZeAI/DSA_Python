def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        ls: list = []
        for i in range(n):
            ls.append(list(map(float, input().split())))
        ans = [1] * n
        m = 1
        for i in range(n):
            for j in range(i):
                if ls[i][0] > ls[j][0] and ls[i][1] < ls[j][1]:
                    ans[i] = max(ans[i], ans[j] + 1)
            m = max(m, ans[i])
        print(m)
main()
