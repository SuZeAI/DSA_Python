def main():
    t: int = int(input())
    while t > 0:
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        ls1: list= list()
        for i in set(ls):
            ls1.append([i, ls.count(i)])
        ls1.sort(key=lambda x: x[1], reverse=True)
        for i in ls1:
            print(f"{i[0]} "*i[1], end="")
        t -= 1
main()