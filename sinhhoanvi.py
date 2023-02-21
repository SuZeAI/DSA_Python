def resulft(ls):
    for i in ls:
        print(i, end="")
    print(end=" ")
def Try(i, n, bl, ls):
    for j in range(n, 0, -1):
        if bl[j]:
            bl[j] = False
            ls.append(j)
            if i == n:
                resulft(ls)
            else:
                Try(i + 1, n, bl, ls)
            bl[j] = True
            ls.pop()

def main():
    t = int(input())
    while t > 0:
        n = int(input())
        bl: list[bool] = [True] * (n + 1)
        ls: list = list()
        Try(1, n, bl, ls)
        print()
        t -= 1
main()