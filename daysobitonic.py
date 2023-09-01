def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        ls_up = [0] * n
        ls_down = [0] * n
        for i in range(n):
            ls_up[i] = ls[i]
            for j in range(i):
                if ls[i] > ls[j] and ls_up[i] < ls_up[j] + ls[i]:
                    ls_up[i] = ls_up[j] + ls[i]
        ls.reverse()
        for i in range(n):
            ls_down[i] = ls[i]
            for j in range(i):
                if ls[i] > ls[j] and ls_down[i] < ls_down[j] + ls[i]:
                    ls_down[i] = ls_down[j] + ls[i]
        ls_down.reverse()
        ls.reverse()
        tu = max(zip(ls_up, ls_down, [i for i in range(n)]), key=lambda x: x[0] + x[1] - ls[x[2]])
        print(tu[0] + tu[1] - ls[tu[2]])
main()