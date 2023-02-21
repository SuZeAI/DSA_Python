# same upper_bound
from bisect import bisect_right, bisect_left
def main():
    t: int= int(input())
    while t > 0:
        n: int= int(input())
        ls: list= list(map(int, input().split()))
        lss = [ls[x] + ls[y] for x in range(len(ls) - 1) for y in range(x + 1, len(ls))]
        print(min(lss, key=lambda x: abs(x)))

        # ls_am = sorted([i for i in ls if i >= 0])
        # ls_dg = sorted([i for i in ls if i < 0])
        # mn = 1e10
        # if not len(ls_am):
        #     mn = min(mn, ls_am[0] + ls_am[1], key=lambda x: abs(x))
        # if not len(ls_dg):
        #     mn = min(mn, ls_dg[0] + ls_dg[1], key=lambda x : abs(x))
        # if (not len(ls_dg)) and (not len(ls_am)):
        #     mn = min(mn, ls_am[0] + ls_dg[0], ls_am[0] + ls_dg[])

        t -= 1
main()