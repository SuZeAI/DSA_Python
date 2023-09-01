def main():
    t: int = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        ls = list(map(int, input().split()))
        ls_1 = ls.copy()
        i = k - 1
        while i >= 0 and ls[i] == n - k + i + 1:
            i -= 1
        if i == -1:
            print(k)
        else:
            ls[i] += 1
            for j in range(i + 1, k):
                ls[j] = ls[i] + j - i
            print(len(set(ls_1).difference(ls)))
    
main()