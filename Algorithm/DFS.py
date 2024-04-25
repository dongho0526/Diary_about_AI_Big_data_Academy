import sys
sys.setrecursionlimit(1000000)

def DFS(v, List, Check):
    if v in Check:
        return
    if v not in Check:
        Check.append(v)
        for i in List[v]:
            if i not in Check:
                DFS(i, List, Check)

t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    List = [[] for _ in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        List[u].append(v)
        List[v].append(u)
    for i in range(N):
        List[i].sort()
    
    Check = []
    DFS(0, List, Check)
    print(*Check)