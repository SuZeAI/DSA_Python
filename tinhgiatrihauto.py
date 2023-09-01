from queue import LifoQueue
def cal(a:int , b: int, c: chr) -> int:
    if c == '+': return a + b
    if c == '-': return a - b
    if c == '*': return a * b
    if c == '/': return a//b
def main() -> None:
    t: int = int(input())
    for _ in range(t):
        s: str = input()
        st: LifoQueue = LifoQueue()
        for i in s:
            if i.isdigit():
                st.put(int(i))
            else:
                s1 = st.get()
                s2 = st.get()
                s3 = cal(s2, s1, i)
                st.put(s3)
        print(st.get())
main()