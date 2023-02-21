# zip() unzip(*x)
# enumerate(ls, idx)
# class T(object):
# ALL is OBJECT
def main():
    t: int= int(input())
    modulo = int(1e9 + 7)
    while t > 0:
        n: int= int(input())
        ls: list= list(map(int, input().split()))
        ls.sort()
        sum = 0
        for idx, vl in enumerate(ls):
            sum = (sum % modulo +  (vl * idx) % modulo) % modulo
        print(sum)
        t -= 1
main()