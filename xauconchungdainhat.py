def main():
    t: int = int(input())
    for _ in range(t):
        s1 = input()
        s2 = input()
        ls: list[list] = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]
        for i in range(1, len(s2) + 1):
            for j in range(1, len(s1) + 1):
                if s2[i - 1] == s1[j - 1]:
                    ls[i][j] = ls[i - 1][j - 1] + 1
                else:
                    ls[i][j] = max(ls[i - 1][j], ls[i][j - 1])
        print(ls[len(s2)][len(s1)])

main()