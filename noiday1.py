# zip() * zip(*)
# class T(object):
# ALL is OBJECT
from queue import PriorityQueue
def main():
    t: int = int(input())
    while t > 0:
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        pri_que = PriorityQueue()
        for i in ls:
            pri_que.put(i)
        m = 0
        while pri_que.qsize() > 1:
            sum = pri_que.get() + pri_que.get()
            m += sum
            pri_que.put(sum)
        print(m)

        t -= 1
main()