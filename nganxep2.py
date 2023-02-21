import sys
def main():
    st = []
    t: int = int(input())
    while t > 0:
        ls = input().split()
        if ls[0] == "PUSH":
            st.append(ls[1])
        elif ls[0] == "POP" and len(st) > 0:
            st.pop()
        elif ls[0] == "PRINT":
            if len(st) == 0:
                print("NONE")
            else:
                print(st[len(st) - 1])

        t -= 1
main()