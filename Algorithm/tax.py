# money = [50000, 10000, 5000, 1000, 500, 100]

# t = int(input())

# for _ in range(t):
#     count = 0
#     query = int(input())
#     for index, elm in enumerate(money):
#         while not query-elm < 0 :
#             query = query-elm
#             count += 1
#     print(count)

money = [50000, 10000, 5000, 1000, 500, 100]

t = int(input())

for _ in range(t):
    count = 0
    query = int(input())
    for index, elm in enumerate(money):
        count += query // elm
        query %= elm

    print(count)