def main():
    t: int = int(input())
    for _ in range(t):
        n = int(input())
        ls1 = list(map(int, input().split()))
        ls2 = list(map(int, input().split()))
        for a, b in enumerate(ls1, 0):
            if b != ls2[a]:
                print(a + 1)
                break
main()