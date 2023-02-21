def main() -> None:
    t: int= int(input())
    while t > 0:
        n, k = map(int, input().split())
        ls: list[int] = list(map(int, input().split()))
        lstmp: list[int] = ls.copy()
        i: int = k - 1
        while i >= 0 and ls[i] == n + i - k + 1:
            i -= 1

        if i == -1:
            print(k)
        else:
            ls[i] += 1
            for j in range(i + 1, k):
                ls[j] = ls[i] + j - i
            cnt: int= 0
            for j in ls:
                if j  not in lstmp:
                    cnt += 1
            print(cnt)
        t -= 1

main()