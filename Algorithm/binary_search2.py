# def binary(data, left, right, q):
#     if left > right:
#         return -1
#     mid = (left + right) // 2
#     if mid == 0:
#         return data[0]
#     elif mid == len(data)-1:
#         return data[len(data)-1]
#     if data[mid] == q:
#         return data[mid]
    
#     elif q < data[mid] and q > data[mid-1]:  # mid보다 작을 때
#         if q - data[mid - 1] <= data[mid] - q:
#             return data[mid-1]
#         else: return data[mid]

#     elif q > data[mid] and q < data[mid+1]: # mid 보다 클 때
#         if  q - data[mid] <= data[mid + 1] - q:
#             return data[mid]
#         else: return data[mid+1]

#     if data[mid] < q:
#         return binary(data, mid+1, right, q)
#     elif data[mid] > q:
#         return binary(data, left, mid-1, q)

# t = int(input())
# for _ in range(t):
#     data = list(map(int, input().split()))
#     query = list(map(int, input().split()))
#     answer = []

#     for q in query:
#         answer.append(binary(data, 0, len(data) - 1, q))

#     print(*answer)

import bisect

def find(l, x):
    i = bisect.bisect_left(l, x)
    if x <= l[0] : return l[0]
    elif x >= l[len(l)-1] : return l[len(l)-1]
    if x - l[i-1] > l[i] - x: return l[i]
    else : return l[i-1]

t = int(input())

for _ in range(t):
    data = list(map(int, input().split()))
    query = list(map(int, input().split()))
    answer = [find(data, x) for x in query]

    print(*answer)