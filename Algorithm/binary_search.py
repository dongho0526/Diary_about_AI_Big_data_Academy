def binary(data, left, right, q):
    if left > right:
        return -1
    mid = (left + right) // 2
    if data[mid] == q:
        return mid
    if data[mid] < q:
        return binary(data, mid+1, right, q)
    elif data[mid] > q:
        return binary(data, left, mid-1, q)

t = int(input())
for _ in range(t):
    data = list(map(int, input().split()))
    query = list(map(int, input().split()))
    answer = []

    for q in query:
        answer.append(binary(data, 0, len(data) - 1, q))

    print(*answer)


# def binary_search(l, find_num):
#     print('aaa',len(l)//2)
#     if l[len(l)//2] == find_num:
#         return l.index(find_num)
#     elif l[len(l)//2] > find_num:
#         binary_search(l[:l.index(find_num)-1], find_num)
#     elif l[len(l)//2] < find_num:
#         binary_search(l[l.index(find_num)+1:], find_num)


# print(binary_search([1, 2, 3, 3, 4, 5], 5))
# t = int(input())

# for _ in range(t):
#     list_a = list(map(int, input().split()))
#     list_b = list(map(int, input().split()))
#     for find_num in list_b:
#         for elm in list_a:
#             if 
