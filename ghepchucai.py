from bisect import bisect_right, bisect_left
from typing import Union, Optional
from collections import Counter, OrderedDict, namedtuple, defaultdict, deque
def resulft(ls):
    s: str = ""
    for i in ls:
        s += chr(i + 64)
    if "A" in s and "E" in s:
        if s[0] == "A" and s[len(s) - 1] == "E":
            print(s)
        if s[0] == "E" and s[len(s) - 1] == "A":
            print(s)
        # if "AE" in s:
        #     print(s)
    elif "A" in s:
        if s[0] == "A" or s[len(s) - 1] == "A":
            print(s)
    elif "E" in s:
        if s[0] == "E" or s[len(s) - 1] == "E":
            print(s)

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
    n = ord(input()) - 64
    bl: list[bool] = [True] * (n + 1)
    ls: list = list()
    Try(1, n, bl, ls)
    print()
main()