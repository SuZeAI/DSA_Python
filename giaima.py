def main() -> None:
    t: int = int(input())
    for _ in range(t):
        s: list = list(map(int, list(input())))
        if s[0] == 0:
            print(0)
            continue
        s = [20] + s
        ls = [0] * (len(s))
        ls[0] = 1
        for i in range(1, len(s)):
            if s[i] == 0:
                if s[i - 1] > 2:
                    ls[len(s) - 1] = 0
                    break
            else:
                ls[i] += ls[i - 1]
            num = s[i - 1] * 10 + s[i]               
            if 10 <= num <= 26:
                ls[i] += ls[i - 2]
        print(ls[len(s) - 1])                    
                
    
main()
