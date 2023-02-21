from typing import Union, Optional
from enum import Enum
from collections import deque, defaultdict, namedtuple, OrderedDict, Counter
def resulft(ls):
    global s
    for i in ls:
        print(s[i - 1], end="")
    print(end=" ")
def Try(i, n, bl, ls):
    for j in range(1, n + 1):
        if bl[j]:
            bl[j] = False
            ls.append(j)
            if i == n:
                resulft(ls)
            else:
                Try(i + 1, n, bl, ls)
            bl[j] = True
            ls.pop()

def main():
    global s
    t = int(input())
    while t > 0:
        s = input()
        n: int= len(s)
        bl: list[bool] = [True] * (n + 1)
        ls: list = list()
        Try(1, n, bl, ls)
        print()
        t -= 1
main()