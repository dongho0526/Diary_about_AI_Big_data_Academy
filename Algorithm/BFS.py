from collections import deque
import sys

def BFS(start, List, Check):
    queue = deque()
    Check.append(start)
    queue.extend(List[start])
    while queue != deque([]):
        a = queue.popleft()
        if a not in Check:
            Check.append(a)
        for elm in List[a]:
            if elm not in Check:
                queue.append(elm)
    return Check

t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    List = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split(' '))
        List[u].append(v)

    for i in range(N):
        List[i].sort()
    
    Check = []
    print(*BFS(0, List, Check))