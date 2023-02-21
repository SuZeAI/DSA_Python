# It prints "Hello PTIT."
import bisect
print("hello")
a = [1, 2, 3, 4, 4, 4, 5]
print(bisect.bisect_left(a,4))
print(bisect.bisect_right(a, 4))
try:
    print(a.index(4))

except ValueError:
    pass
dc = dict()
dc.update({2 : 4}, b=3)
dc['a'] = 1
print(list(dc))
s = "ABCD"
print("A" in s)
from enum import Enum
class T(Enum):
    a = 1
b = T.a
print(b)
def run():
    for i in range(10):
        yield 80
for i in run():
    print(i)
a = "1234565432"
print(a.replace("2", "t"))
print([[0] * 3] * 4)
from multiset import *
print(type(Multiset([1, 2, 3, 4, 3, 3])))
m = n = dict()
m[2] = 8
print(n[2])
a = [1, 3, 2, 6, 4, 5]
def func(x):
    return x
b = sorted(a, key=func)
print(b)
a = "tuyen"
ls = [-1, -2, 1, 2, 3, 4,0]
print(set(ls))
from bisect import bisect_left
a = [2, 2, 3, 4]
print(bisect_left(a, 3, 2, 4))
print(max(a))
import sys
for i in  sys.stdin:
    print(i)
    break
a = 1.234567
print(f"{a: .2f}hgfj")
for i in range(10):
    print(i)
    if i % 4 ==0:
        i += 1
a = 4
b = 5
a, m = b
print(a, m)
import numpy as np
a = np.array([[1, 1], [1, 1]])
print(a%3)
