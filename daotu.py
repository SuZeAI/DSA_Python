def main():
    t: int = int(input())
    while t > 0:
        s = input().split()
        for i in reversed(s):
            print(i, end=" ")
        print()
        t -= 1
main()