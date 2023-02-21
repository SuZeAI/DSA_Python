# zip() unzip(*x)
# class T(objec):
# yield
# ALL is OBJECT
# deuqe, bisetc_right, bisect_left, defaultdict, namedtuple, OrderedDict, Counter
# from enum import Enum
def check(ls, n):
    nus: list = ls.copy()
    l = 0
    r = n - 1
    nus.sort()
    while l < r:
        if ls[l] < ls[r]:
            if nus[l] != ls[l] or nus[r] != ls[r]:
                return False
        else:
            if nus[l] != ls[r] or nus[r] != ls[l]:
                return False
        l += 1
        r -= 1
    return True
def main():
    t: int = int(input())
    while t > 0:
        n: int = int(input())
        ls: list = list(map(int, input().split()))

        if check(ls, n):
            print("Yes")
        else:
            print("No")
        t -= 1
main()