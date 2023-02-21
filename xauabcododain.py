def output():
    for i in lis:
        if i == 1:
            print(end="B")
        else:
            print(end="A")
    print(end=" ")


def Try(i):
    for j in range(2):
        lis.append(j)
        if i == n:
            output()
        else: Try(i + 1)
        lis.pop()

def main():
    global n, lis
    t = int(input())
    while t > 0:
        n = int(input())
        lis = []
        Try(1)
        print()
        t -= 1

main()