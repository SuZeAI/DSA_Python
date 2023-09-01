def backtrack(n, j, ans):
    for i in range(j, 0, -1):
        ans.append(i)
        if i == n :
            s = " ".join(map(str, ans))
            print(f"({s})", end=" ")
        elif i < n:
            backtrack(n - i, i, ans)
        ans.pop()
            
def main():
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        backtrack(n, n, [])
        print()
main()