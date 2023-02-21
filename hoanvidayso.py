def resulft(ls, nums):
    for i in nums:
        print(ls[i], end=" ")

    print()

def Try(i, n, ls, nums, bl):
    for j in range(1, n + 1):
        if bl[j]:
            bl[j] = False
            nums.append(j)
            if i == n:
                resulft(ls, nums)
            else: Try(i + 1, n, ls, nums, bl)
            bl[j] = True
            nums.pop()

def main():
    n: int= int(input())
    ls: list= list(map(int, input().split()))
    ls.sort()
    ls = [0] + ls
    bl: list[bool] = [True] * (n + 1)
    nums: list= list()
    Try(1, n, ls, nums, bl)


main()