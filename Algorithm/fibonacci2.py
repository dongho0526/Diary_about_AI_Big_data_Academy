t = int(input())

for _ in range(t):
    query = int(input())
    fibonacci = [0 for _ in range(max(3, query+1))]
    fibonacci[0], fibonacci[1], fibonacci[2] = 0, 1, 1
    if query == 1 or query == 2:
        print(fibonacci[query])
    else:
        for index in range(3, query+1):
            fibonacci[index] = fibonacci[index-1] + fibonacci[index-2]
        print(fibonacci[-1])

# for index in range(3, 5):
#     print(index)

# def Fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     else: return Fibo(n-1) + Fibo(n-2)

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     print(Fibo(n))