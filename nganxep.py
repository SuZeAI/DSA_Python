# from queue import LifoQueue
import sys
def main():
    # a = LifoQueue()
    # a.put(1)
    # a.put(2)
    # a.put(3)
    # print(a)
    st = []
    for s in sys.stdin:
        ls = s.split()
        if ls[0] == "push":
            st.append(ls[1])
        elif ls[0] == "pop":
            st.pop()
        elif ls[0] == "show":
            if len(st) == 0:
                print("empty")
            else:
                for i in st:
                    print(i, end=" ")
                print()
main()