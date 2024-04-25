t = int(input())

def Find(graph, visited, x, y, n, m):
    if x+1<n:
        if visited[x+1][y] == -1 : visited[x+1][y] = visited[x][y] + graph[x+1][y]
        else: visited[x+1][y] = min(visited[x+1][y], visited[x][y] + graph[x+1][y])

    if y+1<m:
        if visited[x][y+1] == -1 : visited[x][y+1] = visited[x][y] + graph[x][y+1]
        else: visited[x][y+1] = min(visited[x][y+1], visited[x][y] + graph[x][y+1])

    if x+1<n and y+1<m:
        if visited[x+1][y+1] == -1 : visited[x+1][y+1] = visited[x][y] + graph[x+1][y+1]
        else: visited[x+1][y+1] = min(visited[x+1][y+1], visited[x][y] + graph[x+1][y+1])
    return 0


for _ in range(t):
    n, m = map(int, input().split(' '))
    start_x, start_y = 0, 0
    graph = []
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    for row in range(n):
        list_a = list(map(int, input().split(' ')))
        graph.append(list_a)
    visited[0][0] = graph[0][0]

    for x in range(n):
        for y in range(m):
            Find(graph, visited, x, y, n, m)
    print(visited)
    print(visited[n-1][m-1])


t = int(input())

def dynamic_programming(graph, n, m):
    dp = [[float('inf')] * m for _ in range(n)]  # 최단 거리를 저장할 배열 초기화
    dp[0][0] = graph[0][0]  # 시작 정점의 값으로 초기화

    # 위, 왼쪽, 대각선 위의 세 방향으로 이동하면서 최단 거리를 계산
    for i in range(n):
        for j in range(m):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + graph[i][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + graph[i][j])
            if i > 0 and j > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + graph[i][j])

    return dp[n-1][m-1]  # 마지막 정점까지의 최단 거리 반환

for _ in range(t):
    n, m = map(int, input().split())
    graph = []

    # 그래프 정보 입력
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    result = dynamic_programming(graph, n, m)
    print(result)