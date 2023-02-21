def main() -> None:
    n: int = int(input())
    ls: list = list(map(int, input().split()))
    check = []
    for i in ls:
        if i not in check:
            print(i, end=" ")
            check.append(i)
main()