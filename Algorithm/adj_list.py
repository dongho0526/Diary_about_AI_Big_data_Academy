t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    array = [[] for _ in range(N)]
    for _ in range(M):
        list_input = list(map(int, input().split()))
        array[list_input[0]].append(list_input[1])
        array[list_input[1]].append(list_input[0])
    for index in range(N):
        array[index].sort()
        print(*array[index])
    # print(array)
