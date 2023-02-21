def main():
    t: int= int(input())
    while t > 0:
        n: int = int(input())
        ls: list= list(map(int, input().split()))
        cnt = 0
        for i in range(n):
            m = i
            min = ls[i]
            for j in range(i + 1, n):
                if min > ls[j]:
                    min = ls[j]
                    m = j
            if min != ls[i]:
                ls[i], ls[m] = ls[m], ls[i]
                cnt += 1
        print(cnt)
        t -= 1
main()