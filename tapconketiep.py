def main():
    t = int(input())
    while t > 0:
        n, k = map(int, input().split())
        ls: list= list(map(int, input().split()))
        i: int= k - 1
        while i >= 0 and ls[i] == n + i - k + 1:
            i -= 1

        if i == -1:
            for j in range(1, k + 1):
                print(j, end=" ")
        else:
            ls[i] += 1
            for j in range(i + 1, k):
                ls[j] = ls[i] + j - i
            for j in ls:
                print(j, end=" ")
        print()

        t -= 1
main()
