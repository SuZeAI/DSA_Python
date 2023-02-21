MODULO = int(1e9 + 7)
def luythua(n, k):
    if k == 0:
        return 1
    x = luythua(n, int(k/2))
    if k % 2 == 0:
        return (x * x) % MODULO
    else:
        return (((x * x) % MODULO) * n) % MODULO

def main():
    t: int = int(input())
    while t > 0:
        n = input()
        k = ""
        for i in reversed(n):
            k += i
        # m = n
        # k = 0
        # while m != 0:
        #     k = k * 10 + m % 10
        #     m = int(m/10)
        print(luythua(int(n), int(k)))
        t -= 1
main()