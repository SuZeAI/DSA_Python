def main():
    t: int= int(input())
    while t > 0:
        n,k = map(int, input().split())
        ls1: list= list(map(int, input().split()))
        ls2: list= list(map(int, input().split()))
        print(max(ls1) * min(ls2))
        t -= 1

main()