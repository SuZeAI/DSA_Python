def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n = int(input())
        ls: list = list(map(int, input().split()))
        s = sum(ls)
        if s % 2 == 0:
            k = s//2
            ans = [0] * (100000)
            ans[0] = 1
            for i in ls:
                for j in range(s, i - 1, - 1):
                    if ans[j] == 0 and ans[j - i] == 1:
                        ans[j] = 1
            if ans[s]:
                print("YES")
            else:
                print("NO")      
        else:
            print("NO")
main()