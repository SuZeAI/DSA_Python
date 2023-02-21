def main():
    t: int= int(input())
    while t > 0:
        n: int= int(input())
        ls: list= sorted(list(map(int, input().split())))
        for i in ls:
            print(i, end=" ")
        print()


        t -= 1
main()