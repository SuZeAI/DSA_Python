def backtrachgen(ls, res, i, n, tmp, k):
    global cnt
    for j in range(i, n):
        if k == res:
            cnt += 1
            break
        elif ls[j] > tmp:
            backtrachgen(ls, res + 1, j + 1, n, ls[j], k)
        
def main():
    global cnt
    n, k = map(int, input().split())
    ls: list = list(map(int, input().split()))
    cnt = 0
    ls.append(10000000009)
    backtrachgen(ls, 0, 0, n + 1, 0, k)
    print(cnt)
        
main()