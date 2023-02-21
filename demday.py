MODULO = 123456789
def luythua(n, k):
    if k == 1:
        return n
    x = luythua(n, int(k/2))
    if k % 2 == 0:
        return (x * x) % MODULO
    else:
        return (((x * x) % MODULO) * n) % MODULO
def main():
    t: int = int(input())
    while t > 0:
        n = int(input())
        print(luythua(2, n - 1))
        t -= 1

main()