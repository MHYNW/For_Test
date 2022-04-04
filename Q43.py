def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[y] = a
    else:
        parent[x] = b

N, M = map(int, input().split())
graph = []
parent = [0] * N
result = 0
result_saved = 0

for i in range(N):
    parent[i] = i

for _ in range(M):
    start_node, end_node, cost = map(int, input().split())
    graph.append((cost, start_node, end_node))

graph.sort()

for i in graph:
    cost, start_node, end_node = i
    result += cost
    a = find_parent(parent, start_node)
    b = find_parent(parent, end_node)
    if a != b:
        union(parent, start_node, end_node)
        result_saved += cost

print(result - result_saved)




