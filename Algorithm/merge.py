t = int(input())

for _ in range(t):
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    list_c = list_a + list_b
    list_c.sort()
    for index in range(len(list_c)):
        if list_c[index] in list_a:
            list_c[index] = 1
        elif list_c[index] in list_b:
            list_c[index] = 2
    print(*list_c)

# t = int(input())

# for _ in range(t):
#     list_a = list(map(int, input().split()))
#     list_b = list(map(int, input().split()))
#     marked_a = [(x, 1) for x in list_a]
#     marked_b = [(x, 2) for x in list_b]
#     merged = marked_a + marked_b
#     merged.sort()

#     result = [i for _, i in merged]
#     print(*result)