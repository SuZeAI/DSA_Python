def resulft(ls):
    s: str= ""
    for i in ls:
        if i == 1:
            s += "H"
        else:
            s += "A"
    if s[0] == "H" and s[len(s) - 1] == "A":
        sts = s.split("A")
        for i in sts:
            if i.count("H") > 1:
                return
        print(s)

def Try(i,n, ls: list):
    for j in range(2):
        ls.append(j)
        if i == n:
            resulft(ls)
        else: Try(i + 1, n, ls)
        ls.pop()
def main():
    t: int= int(input())
    while t > 0:
        n: int= int(input())
        ls: list= list()
        Try(1,n, ls)
        t -= 1

main()