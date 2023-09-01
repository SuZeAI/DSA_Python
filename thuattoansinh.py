def output():
    for i in lis:
        print(i, end=" ")
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
    Try(1)

main()