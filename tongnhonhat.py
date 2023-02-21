# zip() unzip(*x)
# class T(object):
# ALL is OBJECT

def main():
    t: int = int(input())
    while t > 0:
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        m = int(1e9)
        a = 0
        b = 0
        ls.sort()
        for i in ls:
            tmpa = a
            a = a * 10 + i
            tmpb = b
            b = b * 10 + i
            if a + tmpb > b + tmpa:
                a = tmpa
            else:
                b = tmpb
        print(a + b)

        t -= 1
main()