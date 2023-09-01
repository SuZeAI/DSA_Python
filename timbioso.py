def backtrach(i, ans, ls):
    for j in ["0", "9"]:
        ls.append(j)
        if i == 10:
            ans.append(int("".join(ls)))
        else:
            backtrach(i + 1, ans, ls)
        ls.pop()
def main():
    ans = []
    backtrach(1, ans, [])
    ans.pop(0)
    print(ans)
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        for k in ans:
            if k % n == 0:
                print(k)
                break
     
    
main()