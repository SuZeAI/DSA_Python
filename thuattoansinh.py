def output():
    for i in lis:
        print(i, end=" ");
    if m % 2 == 0:
        for i in range(len(lis) - 1, -1, -1):
            print(lis[i], end=" ")
    else:
        for i in range(len(lis) - 2, -1, -1):
            print(lis[i], end=" ")
    print()

def Try(i):
    for j in range(2):
        lis.append(j)
        if i == n:
            output()
        else: Try(i + 1)
        lis.remove(j)

def main():
    global n,m, lis
    n = int(input())
    lis= []
    m = n
    if n % 2 ==0:
        n = n /2
    else:
        n = int(n/2) + 1
    Try(1)

main()