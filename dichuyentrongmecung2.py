mp = {(0, 1) : 'R', (-1, 0) : 'U', (1, 0): 'D', (0, -1) : 'L'}
def Try(ls,i, j, n, s, ans, check):
    if i == n - 1 and j == n - 1:
       ans.append(s)
       return 
    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        i += a
        j += b
        if 0 <= i < n and 0 <= j < n and ls[i][j] == 1 and check[i][j]:
            check[i][j] = False
            Try(ls, i, j, n, s + mp[(a, b)], ans, check)
            check[i][j] = True
        i -= a 
        j -= b
def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        check = [[True] * n for i in range(n)]
        ls = []
        for i in range(n):
            ls.append(list(map(int, input().split())))
        ans = []
        s = ""
        check[0][0] = False
        Try(ls, 0, 0, n, s, ans, check)
        
        if len(ans) == 0 or ls[0][0] == 0:
            print(-1)
        else:   print(" ".join(sorted(ans)))
    
main()