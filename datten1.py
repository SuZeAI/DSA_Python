def resulft(ls, nums):
    nus: list= ls.copy()
    nus.pop(0)
    for i in nus:
        print(nums[i], end=" ")
    print()

def Try(i, n, k, ls, nums):
    for j in range(ls[i - 1] + 1, n - k + i + 1):
        ls.append(j)
        if i == k:
            resulft(ls, nums)
        else:
            Try(i + 1, n, k, ls, nums)
        ls.pop()
def main():

    n, k = map(int, input().split())
    nums: list= list(input().split())
    nums = list(set(nums))
    nums.sort()
    n = len(nums)
    nums = ["tuyen"] + nums
    ls: list= list()
    ls.append(0)
    Try(1, n, k, ls, nums)

main()