def Prt(ls: list):
    ns: list = ls.copy()
    print("[", end="")
    for i in range(len(ns) - 1):
        print("{} ".format(ns[i]), end="")
    print("{}]".format(ns.pop()))

def main():
    t: int= int(input())
    while t > 0:
        n: int= int(input())
        ls: list = list(map(int, input().split()))
        while n > 1:
            Prt(ls)
            nums: list= []
            for i in range(n - 1):
                nums.append(ls[i] + ls[i + 1])
            ls = nums.copy()
            n -= 1
        print(ls)
        t -= 1
main()