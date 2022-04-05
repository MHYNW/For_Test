import heapq

n = int(input())
q = []
heapq.heappush(q, 1)
count = 0
ugly = 0

for i in range(n):
    new_ugly = heapq.heappop(q)
    if ugly == new_ugly:
        while ugly == new_ugly:
            new_ugly = heapq.heappop(q)


    count += 1
    ugly = new_ugly
    if count == n:
        break
    ugly1 = ugly * 2
    ugly2 = ugly * 3
    ugly3 = ugly * 5
    heapq.heappush(q, ugly1)
    heapq.heappush(q, ugly2)
    heapq.heappush(q, ugly3)

print(ugly)


