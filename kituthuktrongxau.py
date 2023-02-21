def main():
    t: int = int(input())
    while t > 0:
        n, k = map(int, input().split())
        r = 2**n
        l = 0
        if k % 2 != 0:
            print('A')
        else:
            while True:
                mid = (l + r)//2
                if mid == k:
                    print(chr(n + 64))
                    break
                elif mid < k:
                    l = mid
                    n -= 1
                elif mid > k:
                    r = mid
                    n -= 1
        t -= 1

main()
