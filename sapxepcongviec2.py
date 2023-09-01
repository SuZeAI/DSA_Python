def main():
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        ls: list= list()
        for i in range(n):
            s = list(map(int, input().split()))
            ls.append(s)

main()