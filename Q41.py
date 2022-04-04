def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a <= b:
        parent[y] = a
    else:
        parent[x] = b

N, M = map(int, input().split())
parent = [0]*(N + 1)
for i in range(1, N + 1):
    parent[i] = i


for i in range(N):
    graph = list(map(int, input().split()))
    for j in range(N):
        if graph[j] == 1:
            union_parent(parent, i + 1, j + 1)

plan = list(map(int, input().split()))


flag = True    # checking parent flag

for i in range(M - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        flag = False

if flag == True:
    print("YES")
else:
    print("NO")







