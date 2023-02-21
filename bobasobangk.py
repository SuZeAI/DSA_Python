def sumtrip(ls, n, k):
    dic = dict()
    for i in range(len(ls)):
        dic[ls[i]] = [i, 1]
    for i in range(n - 1):
        for j in range(i + 1, n):
            try:
                if dic[k - ls[i] - ls[j]][1] == 1 and dic[k - ls[i] - ls[j]][0] > j :
                    return True
            except:
                pass
    return False
def main():
    t: int = int(input())
    while t > 0:
        n, k = map(int, input().split())
        ls: list = list(map(int, input().split()))
        if sumtrip(ls, n, k):
            print("YES")
        else:
            print("NO")
        t -= 1

main()