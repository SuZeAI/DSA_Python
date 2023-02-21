def main():
    t:  int = int(input())
    while t > 0:
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        ls1 = ls.copy()
        ls1.sort()
        cnt = 0
        while ls1 != ls:
            a = ls.pop(0)
            ls.append(a)
            cnt += 1
        print(cnt)
        t -= 1
main()
