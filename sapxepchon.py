def main():
    n: int = int(input())
    ls: list = list(map(int, input().split()))
    lt = []
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if ls[min] > ls[j]:
                min = j
        ls[min] , ls[i] = ls[i], ls[min]
        s = f"Buoc {i + 1}: "
        for k in ls:
            s += str(k) + " "
        lt.append(s)
    for k in reversed(lt):
        print(k)
main()