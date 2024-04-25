from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    list_a = list(map(int, input().split()))
    queue = deque([])
    list_ans = []

    for i in range(n):
        if list_a[i] > 0:
            queue.append(list_a[i])
        elif list_a[i] == -1:
            list_ans.append(queue.popleft())
    print(*list_ans)
