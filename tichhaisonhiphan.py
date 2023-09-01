def main():
    t: int = int(input())
    for _ in range(t):
        b1, b2 = input().split()
        print(int(b1, 2) * int(b2, 2))
main()