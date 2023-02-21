def main():
    t: int = int(input())
    while t > 0:
        n, k, m = map(int, input().split())
        ls1: list = list(map(int, input().split()))
        ls2: list = list(map(int, input().split()))
        ls3: list = list(map(int, input().split()))
        st: list = sorted(list(set(ls1 + ls2 + ls3)))
        dic1, dic2, dic3 = dict(), dict(), dict()
        check: bool = True
        for j in st:
            dic1[j] = dic2[j] = dic3[j] = 0
        for i in ls1:
            dic1[i] += 1
        for i in ls2:
            dic2[i] += 1
        for i in ls3:
            dic3[i] += 1
        for i in st:
            m = min(dic1[i], dic2[i], dic3[i])
            if m > 0:
                for j in range(m):
                    check = False
                    print(i, end= " ")
        if check:
            print("NO", end="")
        print()
        t -= 1
main()