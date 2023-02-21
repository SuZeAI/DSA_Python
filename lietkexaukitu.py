def resulft(ls):
    for i in range(1, len(ls)):
        print(chr(ls[i] + 65), end="")
    print()

def Try(i, n, k, ls):
    for j in range(ls[i - 1], n):
        ls.append(j)
        if i == k:
            resulft(ls)
        else:
            Try(i + 1, n, k, ls)
        ls.pop()
def main():
    n, k = input().split()
    ls: list = list()
    ls.append(0)
    Try(1, ord(n) - 64, int(k), ls)

main()