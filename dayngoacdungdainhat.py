from queue import LifoQueue
def main() -> None:
    t: int = int(input())
    for _ in range(t):
        s = list(input())
        ls = [False] * len(s)
        st: LifoQueue = LifoQueue()
        for a, b in enumerate(s, 0):
            if b == "(":
                st.put(a)
            else:
                if not st.empty():
                    idx = st.get()
                    ls[a] = True
                    ls[idx] = True
        mx = 0
        cnt = 0
        ls.append(False)
        for bl in ls:
            if bl:
                cnt += 1
            else:
                mx = max(mx, cnt)
                cnt = 0
        print(mx)



main()