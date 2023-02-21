def main():
    t: int = int(input())
    while t > 0:
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        ls = [0] + ls
        ls1 = [0] * (n + 1)
        ls2 = [0] * (n + 1)
        ls1[n] = ls2[n] = n
        for i in range(n - 1, 0, -1):
            if ls[i] > ls[i + 1]:
                ls1[i] = ls1[i + 1]
            else:
                ls1[i] = i
            if ls[i] < ls[i + 1]:
                ls2[i] = ls2[i + 1]
            else:
                ls2[i] = i
        ans = 0
        for i in range(1, n + 1):
            ans = max(ans, ls1[ls2[i]] - i + 1)
        print(ans)


        t -= 1

main()