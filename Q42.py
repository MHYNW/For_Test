G = int(input())
P = int(input())

result = 0

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a > b:
        parent[x] = b
    else:
        parent[y] = a

plane_gate = [0] * (P + 1)
parent = [0] * (G + 1)
for i in range(G + 1):
    parent[i] = i

for i in range(1, P + 1):
    plane_gate[i] = int(input())

for i in range(1, P + 1):
    plane_parent = find_parent(parent, plane_gate[i])
    if plane_parent == 0:
        break
    else:
        union(parent, plane_parent, plane_parent - 1)
        result += 1

print(result)
