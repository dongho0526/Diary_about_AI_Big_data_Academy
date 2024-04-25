def hanoi(n, start, target, plus):
    if n == 1:
        print(start, ' -> ', target)
    else :
        hanoi(n-1, start, plus, target)
        print(start, ' -> ', target)
        hanoi(n-1, plus, target, start)

t = int(input())
for _ in range(t):
    num = int(input())
    hanoi(num, 'A', 'C', 'B')
    
