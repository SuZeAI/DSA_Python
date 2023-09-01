def backtrack(sm, m, i, arr, n, k, s):
    for j in range(m, n + 1):
        sm += j
        if i == k:
            if sm == s:
                arr.append(1)
        else:
            backtrack(sm, j + 1, i + 1, arr, n, k, s)
        sm -= j
        
    
def main() -> None:
    while True:
        n, k, s = map(int, input().split())
        if n == k == s == 0:
            break
        arr = []
        backtrack(0, 1, 1, arr, n, k, s)
        print(len(arr))
    
main()