n= int(input())
a = [[0] * n for _ in range(n)]
for i in range(n):
    ls = map(int, input().split())
    for j in ls:
         a[i][j - 1] = 1
for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print()
