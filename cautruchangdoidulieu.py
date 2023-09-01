def size(qe: list):
    return len(qe)
def empty(qe: list):
    return 'YES' if len(qe) == 0 else 'NO'
def push(qe, k):
    qe.append(k)
def pop(qe: list):
    if len(qe) != 0:
        qe.pop(0)
def get(qe:  list):
    if len(qe) != 0:
        return qe[0]
    else: return -1
def get_end(qe: list):
    if len(qe) != 0:
        return qe[len(qe) - 1]
    else: return -1
def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        qe = list()
        for __ in range(n):
            a = list(map(int, input().split()))
            if a[0] == 1:
                print(size(qe))
            if a[0] == 2:
                print(empty(qe))
            if a[0] == 3:
                push(qe, a[1])
            if a[0] == 4:
                pop(qe)
            if a[0] == 5:
                print(get(qe))
            if a[0] == 6:
                print(get_end(qe))

main()