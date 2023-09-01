def main():
    n: int = int(input())
    ls: list = []
    for i in range(1, n + 1):
        lis = list(map(int, input().split()))
        for j in lis:
            if i < j:
                ls.append([i, j])
    for tmp in ls:
        print(" ".join(map(str, tmp)))


main()