def resulft(ans, k, rlf):
    s = "".join(map(chr, [i + 65 for i in ans]))
    idx = s.find(k)
    if idx != -1 and s.find(k, idx + 1) == -1:
        rlf.append(s)
def genback(i, ans , k, n, rlf):
    for j in range(2):
        ans.append(j)
        if i == n:
            resulft(ans, k, rlf)
        else:
            genback(i + 1, ans, k, n, rlf)
        ans.pop()
def main():
    n, k = map(int, input().split())
    s = "A" * k
    rlf = []
    genback(1, [], s, n, rlf)
    print(len(rlf))
    for i in rlf:
        print(i)
main()