def main():
    t: int = int(input())
    while t > 0:
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        lt = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                if ls[i] > ls[j]:
                    ls[i], ls[j] = ls[j], ls[i]
            s = f"Buoc {i + 1}: "
            for k in ls:
                s += str(k) + " "
            lt.append(s)
        for k in reversed(lt):
            print(k)
        t -= 1

main()