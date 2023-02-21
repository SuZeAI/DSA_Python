def main():
    t: int = int(input())
    while t > 0:
        n: int= int(input())
        ls: list= list(map(int, input().split()))
        nus: list= ls.copy()
        ls.sort()
        for i in range(n):
            if ls[i] != nus[i]:
                print(i + 1, end=" ")
                break
        for i in range(n - 1, -1, -1):
            if ls[i] != nus[i]:
                print(i  + 1)
                break






        t -=1
main()

