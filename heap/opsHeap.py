from multiprocessing.spawn import import_main_path


import heapq

pq = [5, 10, 1, 30, 4]

heapq.heapify(pq)
print(pq)

print(heapq.heappushpop(pq, 2))
print(pq)

print(heapq.heappushpop(pq, 0))
print(pq)

print(heapq.heappushpop(pq, -1))
print(pq)

mylist = ['asfGH', 'TRYT']
print([x.lower() for x in mylist])
