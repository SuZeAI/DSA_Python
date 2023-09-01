def ksnap(i, w, sumvl, sumwt, n, ans: list, vl, wt):
    global FOPT, resulft
    for j in range(2):
        ans.append(j)
        sumwt += j * wt[i]
        sumvl += j * vl[i]
        if i == n - 1 :
            s = sum([ans[g] * vl[g] for g in range(n)])
            if s > FOPT:
                resulft = ans.copy()
                FOPT = s
        elif (sumvl + (w - sumwt)*(vl[i + 1]/wt[i + 1])) > FOPT:
            ksnap(i + 1, w, sumvl, sumwt, n, ans, vl, wt)
        ans.pop()
        sumwt -= j * wt[i]
        sumvl -= j * vl[i]
def main() -> None:
    global FOPT, resulft
    n, w = map(int, input().split())
    vl = list(map(int, input().split()))
    wt = list(map(int, input().split()))
    wt_vl = list(zip(wt, vl))
    wt_vl.sort(key=lambda x : x[1]/x[0])
    wet, vla = zip(*wt_vl)
    FOPT = 0
    resulft = []
    ksnap(0, w, 0, 0, n, [], vla, wet)
    print(FOPT)
    for i in wt:
        print(resulft[wet.index(i)], end=" ")
main()