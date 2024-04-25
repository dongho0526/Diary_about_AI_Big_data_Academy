t = int(input())

bracket_front = ['(', '{', '[']
bracket_back = [')', '}', ']']

for _ in range(t):
    ans = False
    stack = []
    s = input().strip()
    for char in s:
        if char in bracket_front:
            stack.append(char)
        elif char in bracket_back:
            if not stack:
                break
            top = stack.pop()
            if bracket_front.index(top) != bracket_back.index(char):
                break
    else:
        if not stack:
            ans = True
    if ans:
        print('YES')
    else:
        print('NO')



# t = int(input())

# bracket_front = ['(', '{','[']
# bracket_back = [')', '}', ']']

# for _ in range(t):
#     ans = False
#     list_a = list(input().rstrip(''))
#     list_b = list_a.copy()
#     n = 0
#     for index, elm in enumerate(list_a):
#         if len(list_a) % 2 == 1:
#             break
#         if elm in bracket_back:
#             if bracket_back.index(list_b[index-2*n]) == bracket_front.index(list_b[index-2*n-1]):
#                 list_b.pop(index-2*n)
#                 list_b.pop(index-1-2*n)
#                 n += 1
#             else:
#                 break
#     if len(list_b) == 0:
#         ans = True
#     if ans == True:
#         print('YES')
#     else:
#         print('NO')