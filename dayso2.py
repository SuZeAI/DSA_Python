def Prt(ls: list, m, lss):
    # global cnt , id
    # if cnt >= int(m/2):
    #     id = 1
    # cnt += 1
    ns: list = ls.copy()
    s: str= "["
    for i in range(len(ns) - 1):
        s += "{} ".format(ns[i])
    # if id == 0:
    #     s += "{} ]".format(ns.pop())
    # else:
    s += "{}]".format(ns.pop())
    lss.append(s)


def main():
    global id, cnt
    t: int= int(input())
    while t > 0:
        n: int= int(input())
        ls: list = list(map(int, input().split()))
        lss: list = list()
        m = n
        id = 0
        cnt = 0
        while n > 1:
            Prt(ls, m, lss)
            nums: list= []
            for i in range(n - 1):
                nums.append(ls[i] + ls[i + 1])
            ls = nums.copy()
            n -= 1
        lss.append(ls)
        for i in reversed(lss):
            print("{} ".format(i), end="")
        print()
        t -= 1
main()