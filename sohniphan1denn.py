t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(1,n + 1):
        print(bin(i)[2:],end=" ")
    print()