def rs(resulft, tmp) :
    s = ""
    nus: list= tmp.copy()
    nus.pop(0)
    for i in nus:
        s += str(i) + " "
    resulft.append(s)
def Try(i, idx, n, ls, tmp, resulft):
    for j in range(idx - 1, n):
        if ls[j] > tmp[i - 1]:
            tmp.append(ls[j])
            if 2 <= i <= n:
                rs(resulft, tmp)
            Try(i + 1, j + 2, n, ls, tmp, resulft)
            tmp.pop()


def main():
    n: int= int(input())
    ls: list = list(map(int, input().split()))
    resulft = []
    Try(1, 1, n, ls, [0], resulft)
    resulft.sort()
    for i in resulft:
        print(i)

main()