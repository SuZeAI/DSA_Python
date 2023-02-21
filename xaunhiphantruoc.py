def main():
    t: int= int(input())
    while t > 0:
        s = list(input())
        i = len(s) - 1
        while i >=  0:
            if s[i] == "1":
                s[i] = "0"
                break
            else:
                s[i] = "1"
            i -= 1
        for i in s:
            print(i, end="")
        print()

        t -= 1

main()