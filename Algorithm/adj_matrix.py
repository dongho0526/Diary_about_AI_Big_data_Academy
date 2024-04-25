t = int(input())

for _ in range(t):
    N, M = map(int, input().split())
    list_2 = [[0 for col in range(N)] for row in range(N)]
    for _ in range(M):
        list_input = list(map(int, input().split()))
        list_2[list_input[0]][list_input[1]] = list_input[2]

    for i in range(N):
        print(*list_2[i])
