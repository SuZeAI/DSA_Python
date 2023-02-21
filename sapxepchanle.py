def main() -> None:
    n: int = int(input())
    ls: list = list(map(int, input().split()))
    ls1: list = [ls[i] for i in range(n) if i % 2 == 0]
    ls1.sort()
    ls2: list = [ls[i] for i in range(n) if i % 2 != 0]
    ls2.sort(reverse=True)
    i = 0
    j = 0
    cnt = 0
    while True:
        if i < len(ls1):
            print(ls1[i], end=" ")
            i += 1
            cnt += 1
        if cnt == n:
            break
        if j < len(ls2):
            print(ls2[j], end=" ")
            j += 1
            cnt += 1
        if cnt == n:
            break
main()