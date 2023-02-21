from queue import LifoQueue
def check(s):
    st = LifoQueue()
    for i in s:
        if i == '(' or i == '+' or i == '-' or i == '*' or i == '/':
            st.put(i)
        if i == ')':
            if st.qsize() == 0:
                return False
            a = st.get()
            if a == '(':
                return False
            tmp = st.get()
            while tmp != '(' and st.qsize() != 0:
                tmp = st.get()
            if tmp != '(':
                return False

    return True


def main():
    t: int = int(input())
    while t > 0:
        s = input()
        if check(s):
            print("NO")
        else:
            print("YES")
        t -= 1

main()