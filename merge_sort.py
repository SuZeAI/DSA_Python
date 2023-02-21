from typing import Union, Optional
from collections import deque, namedtuple, defaultdict, OrderedDict, Counter
from bisect import bisect_right
def merge(ls, l, r, m):
    ls_left: list= ls[l:(m + 1)]
    ls_right: list= ls[(m + 1):(r + 1)]
    for i in ls_right:
        ls_left.insert(bisect_right(ls_left, i) , i)
    ls[l: (r + 1)] = ls_left

def merger_sort(ls, l, r):
    if l < r:
        m: int= int((l + r) / 2)
        merger_sort(ls, m + 1, r)
        merger_sort(ls, l, m)
        merge(ls, l, r, m)

def main():
    t: int= int(input())
    while t > 0:
        n:int = int(input())
        ls: list= list(map(int, input().split()))
        merger_sort(ls, 0, n - 1)
        for i in ls:
            print(i, end=" ")
        print()
        t -= 1
main()