def main():
    t: int = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        ls = [0] * (n + 1)
        ls[1], ls[2] = 1, 1
        for i in range(3, n + 1):
            ls[i] = ls[i - 2] + ls[i - 1]
        while True:
            if n == 1:
                print("A")
                break
            elif n == 2:
                print("B")
                break
            if k > ls[n - 2]:
                k -= ls[n - 2]
                n -= 1
            else:
                n -= 2

main()