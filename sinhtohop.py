def resulft(ls):
    for i in range(1,len(ls)):
        print(ls[i], end="")
    print(end=" ")

def Try(i, n, k, ls):
    for j in range(ls[i - 1] + 1, n - k + i + 1):
        ls.append(j)
        if i == k:
            resulft(ls)
        else:
            Try(i + 1, n, k, ls)
        ls.pop()
def main():
    t = int(input())
    while t > 0:
        n, k = map(int, input().split())
        ls: list= list()
        ls.append(0)
        Try(1, n, k, ls)
        t -= 1
        print()

main()