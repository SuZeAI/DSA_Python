from queue import Queue
def push(ls, x):
    ls.put(x)
def printfont(ls):
    if not ls.empty():
        a = ls.get()
        ls.put(a)
        return a
    return 'NONE'
def pop(ls):
    if not ls.empty():
        ls.get()
def main():
    q = int(input())
    qe = Queue()
    for _ in range(q):
        ls = input().split()
        if ls[0] == 'PUSH':
            push(qe, ls[1])
        if ls[0] == 'PRINTFRONT':
           print(printfont(qe))
        if ls[0] == 'POP':
            pop(qe)

main()