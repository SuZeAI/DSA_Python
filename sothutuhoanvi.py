def resulft(ls, nums):
    global cnt
    cnt += 1
    if ls == nums:
        print(cnt)
def Try(i, n, bl, ls, nums):
    for j in range(1, n + 1):
        if bl[j]:
            bl[j] = False
            ls.append(j)
            if i == n:
                resulft(ls, nums)
            else:
                Try(i + 1, n, bl, ls, nums)
            bl[j] = True
            ls.pop()

def main():
    t = int(input())
    global cnt
    while t > 0:
        cnt = 0
        n = int(input())
        nums: list= list(map(int, input().split()))
        bl: list[bool] = [True] * (n + 1)
        ls: list = list()
        Try(1, n, bl, ls, nums)
        t -= 1
main()