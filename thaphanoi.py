def tower(n, a, b, c):
    if n == 1:
        print(a,"->",c)
        return
    tower(n - 1,a, c, b )
    tower(1, a, b , c)
    tower(n - 1, b, a, c)
def main():
    n: int= int(input())
    tower(n, "A", "B", "C")

main()