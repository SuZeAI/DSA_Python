def clr(ls: list):
    for i in ls:
        i.clear()
def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        ls: list = list()
        for i in range(4):
            ls.append(list(map(int, input().split())))
        ans = [[-10000] * n for i in range(4)]
        check = [[] for i in range(n)]
        for i in range(4):
            for m in range(i):
                for j in range(n):
                    for k in range(j):
                    ans[i][j] = ls[i][j]
                    if j - k != 1 and ans[i][j] < ans[i][k] + ls[i][j]:
                        check[i][j].append()
                        ans[i][j] = ans[i][k] + ls[i][j]
                        
                    
                
                
                
main()
        #     ls.append(0)
        # ls.pop()
        # mx = -10000
        # ans = [-10000] * (4 * n + 3)
        # for i in range(4 * n + 3):
        #     if i != n and i != 2 * n + 1 and i != 3 * n + 2:
        #         ans[i] = ls[i]
        #         for j in range(i):
        #             if i - j != 1 and i - j != n + 1:
                        
        #                 ans[i] = max(ans[i], ans[j] + ls[i])
        #         mx = max(mx, ans[i])
                
        # print(ans)
        # print(mx)