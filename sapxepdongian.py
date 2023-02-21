def main():
    t: int = int(input())
    while t > 0:
        n: int = int(input())
        ls: list= list(map(int, input().split()))
        lt =[]
        for i in range(n):
            check = True
            for j in range(n - 1):
                if ls[j + 1] < ls[j]:
                    check = False
                    ls[j], ls[j + 1] = ls[j + 1], ls[j]
            if check:
                break
            s = f"Buoc {i + 1}: "
            for k in ls:
                s += str(k) + " "
            lt.append(s)
        for k in reversed(lt):
            print(k)
        t -= 1
main()