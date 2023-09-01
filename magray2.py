def main():
    t: int = int(input())
    for _ in range(t):
        s = input()
        n: int = len(s)
        ls = []
        for i in range(n - 1, -1, - 1):
            arr1 = [0] * (1 << i)
            arr2 = [1] * (1 << i)
            arr3 = []
            for j in range(1<<(n - i - 1)):
                if j % 2 == 0:
                    arr3 += arr1 + arr2
                else:
                    arr3 += arr2 + arr1
            ls.append(arr3)
        ans = []
        for i in zip(*ls):
            ans.append("".join(map(str, i)))
        sn = bin(ans.index(s))[2::]
        while len(sn) != n:
            sn = "0" + sn
        print(sn)
        
main()