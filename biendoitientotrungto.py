from queue import LifoQueue
def main() -> None:
    t: int = int(input())
    for _ in range(t):
        s = list(input())
        s.reverse()
        st: LifoQueue = LifoQueue()
        for i in s:
            if i not in ['+', '-', '*', '/']:
                st.put(i)
            else:
                s1 = st.get()
                s2 = st.get()
                ans = f"({s1}{i}{s2})"
                st.put(ans)
        print(st.get())

main()