def main() -> None:
    t = int(input())
    while t > 0:
        n = int(input())
        ls: list = list(map(int, input().split()))
        i = n - 1
        while i > 0 and ls[i] < ls[i - 1]:
            i -= 1
        if i == 0:
            for k in range(1, n + 1):
                print(k, end=" ")
        else:
            j = n - 1
            i -= 1
            while j > i and ls[j] < ls[i]:
                j -= 1
            ls[j], ls[i] = ls[i], ls[j]
            l, r = i + 1, n - 1
            while r > l:
                ls[r], ls[l] = ls[l], ls[r]
            for k in ls:
                print(k, end=" ")
        print()
        t -= 1

main()