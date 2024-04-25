def Fibo(n):
    if n == 1 or n == 2:
        return 1
    else: return Fibo(n-1) + Fibo(n-2)

t = int(input())
for _ in range(t):
    n = int(input())
    print(Fibo(n))