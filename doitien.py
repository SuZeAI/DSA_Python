# from typing import Optional, Union
# from collections import deque, Counter, namedtuple, defaultdict, OrderedDict
# from bisect import bisect_right, bisect_left
# import cv2
# import torch
# import tensorflow
# zip() unzip(*ls) enumerate(, num)
def main():
    ls_my: list = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    t = int(input())
    while t > 0:
        n: int = int(input())
        i = 9
        cnt = 0
        while True:
            if n >= ls_my[i]:
                cnt += 1
                n -= ls_my[i]
                if n == 0:
                    break
            else:
                i -= 1
        print(cnt)
        t -= 1


main()