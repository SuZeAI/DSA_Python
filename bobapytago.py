def pytago(ls1, l, r, n):
    for i in range(n):
        pass


def main():
    t: int = int(input())
    while t > 0:
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        ls1 = [i**2 for i in ls]

        t -= 1

main()