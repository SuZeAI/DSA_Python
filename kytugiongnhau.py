def Tinh(n, x, y , z):
    f = [0] * 105
    f[1] = x
    for i in range(2, n + 1):
        if(i & 1):
            f[i] = min(f[i - 1] + x, f[(i + 1)//2] + z + y)
        else:
            f[i] = min(f[i - 1] + x, f[i//2] + z)
    return f[n]
def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        x, y, z = map(int, input().split())
        print(Tinh(n,x, y, z))
main()