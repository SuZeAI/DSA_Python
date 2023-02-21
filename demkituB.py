def main():
    t: int = int(input())
    while t > 0:
        n, k = map(int, input().split())
        f0 = "A"
        f1 = "B"
        fn = ""
        if n == 0:
            print(0)
        elif n == 1:
            print(1)
        else:
            for i in range(2, n + 1):
                fn = f1 + f0
                f1, f0 = fn, f1
            cnt = 0
            for i in range(0, k):
                if fn[i] == "B":
                    cnt += 1
            print(cnt)
        t -= 1

main()