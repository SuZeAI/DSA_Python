from collections import Counter
def main():
    t: int = int(input())
    while t > 0:
        n: int = int(input())
        s: str = input()
        cnt = Counter(s)
        ls: list = list()
        for a, b in cnt.items():
            ls.append([a, b])
        ls.sort(key=lambda x: x[1], reverse=True)
        stmp: list = [' ']*len(s)
        i = 0
        for a, b in ls:
            dem = 0
            for j in range(i, len(s), n):
                stmp[j] = a
                dem += 1
                if dem == b:
                    break
            while i < len(s) and stmp[i] != ' ':
                i += 1

        if ' ' in stmp:
            print(-1)
        else:
            print(1)
        t -= 1

main()