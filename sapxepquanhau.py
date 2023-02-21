def nqueen(i, n, bl_xuoi, bl_ngc, bl, resulft):
    for j in range(1, n + 1):
        if bl[j] and bl_ngc[i - j + n] and bl_xuoi[i + j - 1]:
            bl[j] = bl_ngc[i - j + n] = bl_xuoi[i + j - 1] = False
            if i == n:
                resulft.append(1)
            else:
                nqueen(i + 1, n, bl_xuoi, bl_ngc, bl, resulft)
            bl[j] = bl_ngc[i - j + n] = bl_xuoi[i + j - 1] = True

def main():
    t: int = int(input())
    while t > 0:
        n: int = int(input())
        bl: list[bool] = [True] * (n + 1)
        bl_xuoi = [True] * (2 * n + 1)
        bl_ngc = [True] * (2 * n + 1)
        resulft = []
        nqueen(1, n, bl_xuoi, bl_ngc, bl, resulft)
        print(len(resulft))
        t -= 1

main()