def resulft(ls):
    nus: list= ls.copy()
    nus.pop(0)
    for i in nus:
        print(chr(i + 64), end="")
    print()

def Try(i, n, k, ls):
    for j in range(ls[i - 1] + 1, n - k + i + 1):
        ls.append(j)
        if i == k:
            resulft(ls)
        else:
            Try(i + 1, n, k, ls)
        ls.pop()
def main():
    t: int= int(input())
    while t > 0:

        n, k = map(int, input().split())
        ls: list= list()
        ls.append(0)
        Try(1, n, k, ls)

        t -= 1

main()