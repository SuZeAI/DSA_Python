def main():
    t: int = int(input())
    while t > 0:
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        check = True
        dic = dict()
        for i in ls:
            dic[i] = 0
        for i in ls:
            dic[i] += 1
        for i in ls:
            if dic[i] > 1:
                check = False
                print(i)
                break
        if check:
            print("NO")

        t -= 1

main()