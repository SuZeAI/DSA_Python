# zip(): merge zip(*x): not merge
# class T(object):
# ALL is OBJECT
# yield


def main() -> None:
    t: int = int(input())
    while t > 0:
        n: int = int(input())
        ls: list = list()
        ls1: list = list()
        for i in range(n):
            a, b = map(int, input().split())
            ls.append(a)
            ls1.append(b)
        merger_ls: list = list(zip(ls, ls1))
        merger_ls.sort(key=lambda x: x[1])
        cnt = 0
        tmp = 0
        for a, b in merger_ls:
            if tmp <= a:
                tmp = b
                cnt += 1
        print(cnt)
        t -= 1
main()