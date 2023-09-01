from queue import LifoQueue
def check(c):
    return c in "+-*/^"
def char(c):
    return ('A' <= c <= 'Z' or 'a' <= c <= 'z')
def deg(c):
    if c == '^':
        return 3
    if c == '*' or c == '/':
        return 2
    if c == '+' or c == '-':
        return 1
    return 0
def main() -> None:
    t: int = int(input())
    for _ in range(t):
        s = list(input())
        n = len(s)
        ans = ""
        st = LifoQueue()
        for i in s:
            if i == '(':
                st.put(i)
                continue
            if i == ')':
                c = st.get()
                while c != '(':
                    ans += c
                    c = st.get()
                continue
            if char(i):
                ans += i
                continue
            if check(i):
                c = st.get()
                while deg(c) >= deg(i):
                    ans += c
                    c = st.get()
                st.put(c)
                st.put(i)
                continue
        while not st.empty():
            ans += st.get()
        print(ans)






main()