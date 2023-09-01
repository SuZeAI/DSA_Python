def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        ls: list = []
        for i in range(n):
            ls.append(list(map(float, input().split())))
        print(ls)
main()