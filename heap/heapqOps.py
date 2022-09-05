import heapq

pq = [5, 20, 1, 30, 4]

heapq.heapify(pq)
print(pq)

heapq.heappush(pq, 3)
print(pq)

print(heapq.heappop(pq))
print(pq)

print(heapq.nlargest(2, pq))

print(heapq.nsmallest(2, pq))
