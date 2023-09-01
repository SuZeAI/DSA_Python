from queue import LifoQueue
def main() -> None:
    t: int = int(input())
    for _ in range(t):
        s = list(input())
        st: LifoQueue = LifoQueue()
        s.reverse()
        for i in s:
            if i not in ['+', '-', '*', '/']:
                st.put(i)
            else:
                s1 = st.get()
                s2 = st.get()
                tmp = f"{s1}{s2}{i}"
                st.put(tmp)
        print(st.get())

main()