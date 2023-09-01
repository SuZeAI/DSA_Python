def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        ls_up = [0] * n
        ls_down = [0] * n
        ls_up[n - 1] = n - 1
        ls_down[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            if ls[i] < ls[i + 1]:
                 ls_up[i] = ls[i + 1]
            else:
                ls_up[i] = i
            if ls[i] > ls[i  + 1]:
                ls_down[i] = ls_down[i + 1]
            else:
                ls_down[i] = i
        ans = 0
        for i in range(n):
            ans = max(ans, ls_down[ls_up[i]] - i + 1)
        print(ans)
main()