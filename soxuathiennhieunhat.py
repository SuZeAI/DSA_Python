def main():
    t: int = int(input())
    while t > 0:
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        dic = dict()
        for i in set(ls):
            dic[i] = 0
        for i in ls:
            dic[i] += 1
        m = 0
        vl = 0
        for a, b in dic.items():
            if m < b:
                m = b
                vl = a
        if m > n/2:
            print(vl)
        else:
            print("NO")

        t -= 1

main()