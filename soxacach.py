def resulft(ls):
    for i in range(len(ls) - 1):
        if abs(ls[i + 1] - ls[i]) == 1:
            return

    for i in ls:
        print(i,end="")
    print()
def Try(i, n, bl, ls):
    for j in range(1, n + 1):
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