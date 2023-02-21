def resulft(ls):
    s: str = ""
    for i in ls:
        if i == 1:
            s += "8"
        else:
            s += "6"
    if s[0] == "8" and s[len(s) - 1] == "6":
        nums: list= s.split("6")
        for i in nums:
            if i.count("8") > 1:
                return
        nums1: list= s.split("8")
        for i in nums1:
            if i.count("6") > 3:
                return
        print(s)


def Try(i, k, ls: list):
    for j in range(2):
        ls.append(j)
        if i == k:
            resulft(ls)
        else: Try(i + 1, k, ls)
        ls.pop()
def main():
    n: int= int(input())
    ls: list= list()
    Try(1,n, ls)

main()