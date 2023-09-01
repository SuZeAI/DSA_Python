# ALL ARE OBJECT and ALL ARE ASSIGNED TO ADDRESS
def main() -> None:
    t: int = int(input())
    for _ in range(t):
        s: str = input()
        n = len(s)
        ls: list = [0] * n
        ls[0] = int(s[0])
        num: int = int(s[0])
        for i in range(1, n):
            num = num * 10 + (i + 1) * int(s[i])
            ls[i] += ls[i - 1] + num
        print(ls[n - 1])

main()