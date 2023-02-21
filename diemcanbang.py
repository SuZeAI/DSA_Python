def main():
    t: int = int(input())
    while t > 0:
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        ls1 = []
        sum1 = 0
        for i in ls:
            sum1 += i
            ls1.append(sum1)
        ls2 = []
        sum2 = 0
        for i in reversed(ls):
            sum2 += i
            ls2.append(sum2)
        ls2.reverse()
        check = True
        for i in range(len(ls1)):
            if ls1[i] == ls2[i]:
                print(i + 1)
                check = False
                break
        if check:
            print(-1)
        t -= 1
main()