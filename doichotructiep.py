def main():
    n: int = int(input())
    ls: list = list(map(int, input().split()))
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if ls[min] > ls[j]:
                min = j
        ls[min] , ls[i] = ls[i], ls[min]
        print(f"Buoc {i + 1}: ", end= "")
        for k in ls:
            print(k, end=" ")
        print()
main()