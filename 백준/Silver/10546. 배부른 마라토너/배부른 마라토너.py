N = int(input())

dictionary = {}

for i in range(N):
    name = input()
    if name in dictionary:
        dictionary[name] += 1
    else:
        dictionary[name] = 1

for i in range(N-1):
    name = input()
    if dictionary[name] == 1:
        del dictionary[name]
    elif name in dictionary:
        dictionary[name] -= 1

print(*dictionary)