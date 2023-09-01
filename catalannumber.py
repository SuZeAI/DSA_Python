def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        c = [0] * (n + 1)
        c[0] = 1
        c[1] = 1
        for i in range(2, n + 1):
            for j in range(0, i):
                c[i] += c[j] * c[i - j - 1]
        print(c[n])

main()