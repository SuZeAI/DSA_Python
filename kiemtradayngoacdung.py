from queue import LifoQueue
def exam(s) -> bool:
    st = LifoQueue()
    for i in s:
        if i == "(" or i == "[" or i == "{":
            st.put(i)
        else:
            if st.qsize() == 0:
                return False
            c = st.get()
            if i == ")" and c != "(":
                return False
            if i == "}" and c != "{":
                return False
            if i == "]" and c != "[":
                return False
    return True
def main() -> None:
    t: int = int(input())
    for _ in range(t):
        s = input()
        if exam(s):
            print("YES")
        else:
            print("NO")

main()