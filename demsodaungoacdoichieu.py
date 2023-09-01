from queue import LifoQueue
def solution(s) -> int:
    st = LifoQueue()
    res = 0
    for i in s:
        if i == '(':
            st.put(i)
        else:
            if st.empty():
                res += 1
                st.put('(')
            else:
                st.get()
    if not st.empty():
        res += st.qsize() //2
    return res

def main() -> None:
    t: int = int(input())
    for _ in range(t):
        s: str = input()
        print(solution(s))

main()