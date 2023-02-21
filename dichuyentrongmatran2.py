from typing import Optional, Union
from enum import Enum
from collections import Counter, namedtuple, defaultdict, OrderedDict, deque
def Try(n, m, x, y, resulft):
    for a, b in [[1, 0], [0, 1]]:
        x += a
        y += b
        if 0 <= x < n and 0 <= y < m:
            if x == n - 1 and y == m - 1:
                resulft.append(1)
            else:
                Try(n,m, x, y, resulft)
        x -= a
        y -= b


def main():
    t: int= int(input())
    while t > 0:
        n, m = map(int, input().split())
        lss: list= []
        for i in range(n):
            lss.append(list(map(int, input().split())))
        resulft: list= list()
        Try(n,m, 0,  0, resulft)
        print(len(resulft))
        t -= 1
main()

