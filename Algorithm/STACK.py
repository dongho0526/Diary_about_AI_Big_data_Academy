n = int(input())

for _ in range(n):
    a = int(input())
    list_a = list(map(int, input().split()))
    list_b = []
    list_c = []
    for i in range(a):
        if list_a[i] > 0:
            list_b.append(list_a[i])
        elif list_a[i] == -1:
            list_c.append(list_b.pop())
    print(*list_c)




# n = int(input())

# for _ in range(n):
#     a = int(input())
#     list_a = list(map(int, input().split()))
#     list_c = []
#     for num in reversed(list_a):
#         if num == -1:
#             list_a.pop()
#             list_c.append(list_a.pop())
#     print(*list_c[::-1])