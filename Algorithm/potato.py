# False인 경우 정상, True일 경우 불량
def inspect(n):
    check = [True for i in n[-5:] if i <= 20 or i >= 80]
    return sum(check)

t = int(input())

for _ in range(t):
    list_input = list(map(int, input().split(' ')))
    list_copy = []
    count = 0
    for index, elm in enumerate(list_input):
        if elm >= 0:
            list_copy.append(elm)
        elif elm == -1:
            count += inspect(list_copy[-5:])
            del list_copy[-5:]
    print(count)
