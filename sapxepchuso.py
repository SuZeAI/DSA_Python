from enum import Enum
from typing import Union, Optional
from collections import deque, defaultdict, namedtuple, OrderedDict, Counter
import torch
def main():
    t: int= int(input())
    while t > 0:
        n: int= int(input())
        ls: list= list(map(int, input().split()))
        st: set= set()
        for i in ls:
            st.update(list(str(i)))
        ls = list(st)
        ls.sort()
        for i in ls:
            print(i, end=" ")
        print()
        t -= 1
main()