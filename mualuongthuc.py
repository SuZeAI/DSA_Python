# ALL Is OBJECT
def main():
    t: int = int(input())
    while t > 0:
        n, s, m = map(int, input().split())
        if s * m > (s - s//7) * n:
            print(-1)
        else:
            for i in range(1, s - s//7 + 1):
                if n * i >= s * n:
                    print(i)
                    break
        t -= 1


main()