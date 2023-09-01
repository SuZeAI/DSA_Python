n =  int(input())
ls = []
for _ in range(n):
    ls.append(list(map(int, input().split())))
for i in range(n):
    for k in range(len(ls[i])):
        if ls[i][k] == 1:
            print(k + 1, end=" ")
    print()
            