def main():
    n: int = int(input())
    ls: list = list(map(int, input().split()))
    nus = []
    ls_str = []
    for i in range(n):
        s = f"Buoc {i}: "
        nus.append(ls[i])
        nus.sort()
        for j in nus:
            s += str(j) + " "
        ls_str.append(s)
    for tmp in reversed(ls_str):
        print(tmp)
main()