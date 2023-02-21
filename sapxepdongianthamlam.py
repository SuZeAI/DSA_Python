# ALL is OBJECT
def Max_len(ls, n):
    max_len = 0
    lis = [0] * (n + 1)
    for i in range(n):
        lis[ls[i]] = lis[ls[i] - 1] + 1
        max_len = max(max_len, lis[ls[i]])
    return max_len
def main():
    n: int = int(input())
    ls: list = list(map(int, input().split()))
    print(n - Max_len(ls, n))

main()