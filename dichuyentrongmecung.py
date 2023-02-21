from typing import Optional, Union
from enum import Enum
from collections import Counter, namedtuple, defaultdict, OrderedDict, deque
def Try(n, x, y, lss, s, resulft):
    for a, b in [[1, 0], [0, 1]]:
        x += a
        y += b
        print(x, y)
        tmp = s
        if 0 <= x < n and 0 <= y < n and lss[x][y] == 1 :
            if a == 1:
                s += "D"
            else:
                s += "R"
            print(x, y)
            if x == n - 1 and y == n - 1:
                resulft.append(s)
            else:
                Try(n, x, y, lss, s, resulft)
        s = tmp
        x -= a
        y -= b


def main():
    t: int= int(input())
    while t > 0:
        n = int(input())
        lss: list= []
        for i in range(n):
            lss.append(list(map(int, input().split())))
        resulft: list= list()
        if lss[0][0]:
            Try(n, 0,  0, lss, "", resulft)
        if not len(resulft) :
            print(-1,end="")
        else:
            for i in resulft:
                print(i, end=" ")
        print()
        t -= 1
main()

