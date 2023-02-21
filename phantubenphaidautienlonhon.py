def main():
    t: int = int(input())
    while t > 0:
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        ls2 = [-1] * n
        st = []
        for i in range(n):
            while len(st) != 0 and ls[i] > ls[st[len(st) - 1]]:
                ls2[st[len(st) - 1]] = i
                st.pop()
            st.append(i)
        for i in range(n):
            if ls2[i] == -1:
                print(-1, end=" ")
            else:
                print(ls[ls2[i]], end=" ")
        print()
        t -= 1
main()