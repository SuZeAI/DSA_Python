# def main():
#     t: int = int(input())
#     while t > 0:
#         v, e = map(int, input().split())
#         dic_v = dict()
#         for i in range(1, v + 1):
#             dic_v[i] = set()
#         for i in range(e):
#             f, l = map(int, input().split())
#             dic_v[f].add(l)
#             dic_v[l].add(f)
#         for a, b in dic_v.items():
#             print(a, end=": ")
#             for i in b:
#                 print(i, end=" ")
#             print()
#         t -= 1
#
# main()
def convert_to_adj_list(num_vertices, edge_list):
    adj_list = {}
    for i in range(1, num_vertices+1):
        adj_list[i] = []
    for e in edge_list:
        adj_list[e[0]].append(e[1])
        adj_list[e[1]].append(e[0])
    return adj_list

t = int(input())
for _ in range(t):
    num_vertices, num_edges = map(int, input().split())
    edge_list = [list(map(int, input().split())) for _ in range(num_edges)]
    adj_list = convert_to_adj_list(num_vertices, edge_list)
    for i in range(1, num_vertices+1):
        print("{}: {}".format(i, ' '.join(map(str, adj_list[i]))))
