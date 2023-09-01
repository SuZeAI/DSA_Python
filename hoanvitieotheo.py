def main():
    t: int = int(input())
    for _ in range(t):
        test, s = input().split()
        print(test, end=" ")
        # n = list(map(int, list(s)))
        # print(n)
        n= list(map(int,list(s)))
        l = len(n)
        i = l - 1
        while i > 0 and n[i] <= n[i - 1]:
            i -= 1
        if i == 0:
            print("BIGGEST")
        else:
            i -= 1
            idx = l - 1
            while idx > i and n[idx] <= n[i]:
                idx -= 1
            n[i], n[idx] = n[idx], n[i]
            lf = i + 1
            r = l - 1
            while lf < r:
                n[lf], n[r] = n[r], n[lf]
                lf += 1
                r -= 1
            print("".join(map(str, n)))
    
main()