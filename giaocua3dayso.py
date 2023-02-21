def main():
    t: int = int(input())
    while t > 0:
        n, m, k = map(int, input().split())
        ls1: list = list(map(int, input().split()))
        ls2: list = list(map(int, input().split()))
        ls3: list = list(map(int, input().split()))
        i = j = h = 0
        ls: list = list()
        while i < n and j < m and h < k:
            if ls1[i] == ls2[j] == ls3[h]:
                ls.append(ls1[i])
                i += 1
                j += 1
                h += 1
            elif ls1[i] < ls2[j]:
                i += 1
            elif ls2[j] < ls3[h]:
                j += 1
            else:
                h += 1
        if not len(ls):
            print(-1)
        else:
            print(" ".join(list(map(str, ls))))

        t -= 1
main()