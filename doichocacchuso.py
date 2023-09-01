def main() -> None:
    t: int = int(input())
    for _ in range(t):
        k: int = int(input())
        s = list(input())
        n = len(s)
        for i in range(k):
            l = 0; r = n - 1; tmp = r
            while l < r and s[l + 1] <= s[l]:
                l += 1
            while l < r:
                if s[r] > s[tmp]:
                    tmp = r
                r -= 1
            l = 0
            while l < tmp and s[l] >= s[tmp]:
                 l += 1
            s[l], s[tmp] = s[tmp], s[l]
        print("".join(s))
    
    
main()