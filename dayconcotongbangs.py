def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        ls: list = list(map(int, input().split()))
        ans = [0] * (s + 5)
        ans[0] = 1
        for i in ls:
            for j in range(s, i - 1, - 1):
                if ans[j] == 0 and ans[j - i] == 1:
                    ans[j] = 1
        if ans[s]:
            print("YES")
        else:
            print("NO")      
    
main()