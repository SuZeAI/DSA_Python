# zip() unzip(*x)
# class T(object)
# ALL is OBJECT
# yield
# from typing import Union, Optional
# from collections import deque, OrderedDict, defaultdict, namedtuple, Counter
# from bisect import bisect_right, bisect_left
def main():
    t: int = int(input())
    while t > 0:
        n, k = map(int, input().split())
        ls: list= list(map(int, input().split()))
        ls.sort()
        sum = 0
        for i in range(min(k, n - k)):
            sum -= ls[i]
        for i in range(min(k, n - k), n):
            sum += ls[i]
        print(sum)
        t -= 1
main()