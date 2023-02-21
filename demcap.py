from typing import Union, Optional
from collections import deque, namedtuple, OrderedDict, defaultdict, Counter
from bisect import bisect_left, bisect_right
import math
def count(x, ls2, n, ls):
    if x == 0:
        return 0
    if x == 1:
        return ls[0]
    ans = n - bisect_right(ls2, x)
    ans += ls[0] + ls[1]
    if x == 2:
        ans -= (ls[3] + ls[4])
    if x == 3:
        ans += ls[2]
    return ans

def main():
    t: int= int(input())
    while t > 0:
        n, m = map(int, input().split())
        ls1: list= list(map(int, input().split()))
        ls2: list= list(map(int, input().split()))
        ls = [0] * 5
        for i in range(len(ls2)):
            if ls2[i] < 5:
                ls[ls2[i]] += 1
        ls2.sort()
        cnt = 0
        for j in range(len(ls2)):
            cnt += count(ls1[j], ls2, n, ls)
        print(cnt)
        t -= 1

main()