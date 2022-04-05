import heapq

N = int(input())

q = []

for _ in range(N):
    data = int(input())
    heapq.heappush(q, data)

result = 0

while q:
    new_card1 = heapq.heappop(q)
    new_card2 = heapq.heappop(q)
    result += new_card1 + new_card2
    heapq.heappush(q, result)
    if len(q) == 1:
        break

print(result)









