def resulft(a: list, k, ls):
    global cnt
    sum: int = 0
    for i in range(len(a)):
        sum += a[i] * ls[i]
    if sum == k:
        for i in range(len(a)):
            if a[i] == 1:
                print(ls[i], end=" ")
        cnt += 1
        print()


def Try(i, n, k, a, ls):
    for j in range(2):
        a.append(j)
        if i == n:
            resulft(a, k, ls)
        else:
            Try(i + 1, n, k, a, ls)
        a.pop()

def main():
    global cnt

    cnt = 0
    n, k = map(int, input().split())
    ls: list = list(map(int, input().split()))
    a: list = list()
    Try(1, n, k, a, ls)
    print(cnt)



main()