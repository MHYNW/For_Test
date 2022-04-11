def find_parents(parents, x):
    if parents[x] != x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    a = find_parents(parents, x)
    b = find_parents(parents, y)
    if a < b:
        parents[y] = a
    else:
        parents[x] = b

N = int(input())

planetXs = []
planetYs = []
planetZs = []
parents = [0] * N

for i in range(N):
    x, y, z = map(int, input().split())
    planetXs.append((x, i))
    planetYs.append((y, i))
    planetZs.append((z, i))
    parents[i] = i

planetXs.sort()
planetYs.sort()
planetZs.sort()
planet_array = []

for i in range(N - 1):
    planet_array.append((planetXs[i + 1][0] - planetXs[i][0], planetXs[i][1], planetXs[i + 1][1]))
    planet_array.append((planetYs[i + 1][0] - planetYs[i][0], planetYs[i][1], planetYs[i + 1][1]))
    planet_array.append((planetZs[i + 1][0] - planetZs[i][0], planetZs[i][1], planetZs[i + 1][1]))

planet_array.sort()
result = 0

for planets in planet_array:
    cost, a, b = planets
    if find_parents(parents, a) != find_parents(parents, b):
        union(parents, a, b)
        result += cost

print(result)




