# zip() zip(*)
# ALL is OBJECT

def main():
    t: int = int(input())
    while t > 0:
        n, k = map(int, input().split())
        ls: list = list(map(int, input().split()))
        dic: dict = dict()
        for i in ls:
            dic[i] = 0
            dic[k - i] = 0
        for i in ls:
            dic[i] += 1
        cnt = 0
        for i in ls:
            dic[i] -= 1
            cnt += dic[k - i]
        print(cnt)
        t -= 1
main()