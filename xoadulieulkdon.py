from collections import Counter, namedtuple,  defaultdict, OrderedDict,  deque
from enum import Enum

def main():
    n: int= int(input())
    ls: list= list(map(int, input().split()))
    rm: int= int(input())
    while rm in ls:
        ls.remove(rm)
    for i in ls:
        print(i, end=" ")

main()