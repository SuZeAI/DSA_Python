def main():
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        Sum = 0
        Max = -100000000
        for i in ls:
            Sum += i
            if Sum < 0:
                Sum = 0
            if Sum > Max:
                Max = Sum
        print(Max)
main()