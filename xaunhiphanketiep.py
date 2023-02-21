def main():
    t = int(input())
    while t > 0:
        s: list= list(input())
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                s[i] = "1"
                break
            else:
                s[i] = "0"
        for i in s:
            print(i, end="")
        print()
        t -= 1
main()