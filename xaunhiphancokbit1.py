def resulft(ls):
    for i in ls:
        print(i, end="")
    print()

def Try(i,n, k, ls: list):
    for j in range(2):
        ls.append(j)
        if i == n:
            if ls.count(1) == k:
                resulft(ls)
        else: Try(i + 1, n, k, ls)
        ls.pop()
def main():
    t: int= int(input())
    while t > 0:
        n, k = map(int, input().split())
        ls: list= list()
        Try(1,n, k, ls)

        t -= 1

main()