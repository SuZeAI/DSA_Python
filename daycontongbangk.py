from enum import Enum
from collections import deque, namedtuple, defaultdict, OrderedDict, Counter
# import cv2
# import torch
# import tensorflow
def resulft(lss):
    nus: list= lss.copy()
    print("[", end="")
    for i in range(len(nus) - 1):
        print(nus[i], end=" ")
    print("{}] ".format(nus.pop()), end="")

def Try(i,  n, k,sum, lss, ls):
    global  check
    for j in range(i - 1, n):
        sum += ls[j]
        lss.append(ls[j])
        if sum == k:
            check = False
            resulft(lss)
        if sum < k:
            Try(j + 2, n, k, sum, lss, ls)
        sum -= ls[j]
        lss.pop()

def main():
    global check
    t: int= int(input())
    while t > 0:
        n, k = map(int, input().split())
        ls: list= list(map(int, input().split()))
        ls.sort()
        check= True

        Try(1, n, k, 0, [], ls)
        if check:
            print(-1)
        else:
            print()
        t -= 1

main()