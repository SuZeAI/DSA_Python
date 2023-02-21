def main():
    bl: list[bool] = [True] * int(1e6)
    bl[0] = False
    bl[1] = False
    for i in range(2, int(1e3),1):
        if bl[i]:
            for j in range(i * i, int(1e6), i):
                bl[j] = False
    t: int = int(input())
    while t > 0:
        check: bool = True
        n: int = int(input())
        for i in range(2, n):
            if bl[i] and bl[n - i]:
                check = False
                print(i, n - i)
                break
        if check:
            print(-1)
        t -= 1


main()