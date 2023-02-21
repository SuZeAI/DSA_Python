def resulft(ls, nums):
    global cnt
    cnt += 1
    if ls == nums:
        print(cnt)


def Try(i, n, k, ls, nums):
    for j in range(ls[i - 1] + 1, n - k + i + 1):
        ls.append(j)
        if i == k:
            resulft(ls, nums)
        else:
            Try(i + 1, n, k, ls, nums)
        ls.pop()
def main():
    global cnt
    t = int(input())
    while t > 0:
        cnt = 0
        n, k = map(int, input().split())
        nums: list= list(map(int, input().split()))
        nums = [0] + nums
        ls: list= list()
        ls.append(0)
        Try(1, n, k, ls, nums)
        t -= 1

main()