def resulft(ls):
    global nums
    nus: list= ls.copy()
    nus.pop(0)
    for i in nus:
        print(nums[i], end=" ")
    print()

def Try(i, n, k, ls):
    for j in range(ls[i - 1] + 1, n - k + i + 1):
        ls.append(j)
        if i == k:
            resulft(ls)
        else:
            Try(i + 1, n, k, ls)
        ls.pop()
def main():
    global nums
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums = list(set(nums))
    nums.sort()
    n = len(nums)
    nums = [0] + nums
    ls: list= list()
    ls.append(0)
    Try(1, n, k, ls)

main()