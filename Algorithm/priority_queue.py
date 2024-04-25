import heapq

t = int(input())

for _ in range(t):
    n = int(input())
    list_a = list(map(int, input().split()))
    heap = []
    list_ans = []
    for elm in list_a:
        if elm > 0 :
            heapq.heappush(heap, elm)
        elif elm == -1:
            list_ans.append(heapq.heappop(heap))
    print(*list_ans)