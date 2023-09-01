def resulft(ans):
    print("["+" ".join(map(str, ans))+"]", end=' ')

def backtrack(check, ls, ans, j, n, x):
    for i in range(j, n):
        ans.append(ls[i])
        if ls[i] == x:
            resulft(ans)
            check.append(1)
        elif ls[i] < x:
            backtrack(check, ls, ans, i, n, x - ls[i])
        ans.pop()

def main():
    t: int = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        ls: list = list(map(int, input().split()))
        ls.sort()
        check = []
        backtrack(check, ls, [], 0, n, x)
        if len(check) == 0:
            print(-1, end="")
        print()
main()