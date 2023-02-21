def countTriplets(ls, n, sum):
    ls.sort()
    ans = 0
    for i in range(0, n - 2):
        j = i + 1
        k = n - 1
        while j < k:
            if ls[i] + ls[j] + ls[k] >= sum:
                k = k - 1
            else:
                ans += (k - j)
                j = j + 1
    return ans
def main():
    t: int = int(input())
    while t > 0:
        n, k = map(int, input().split())
        ls: list = list(map(int, input().split()))
        print(countTriplets(ls, n, k))
        t -= 1

    
main()