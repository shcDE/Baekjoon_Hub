N = input()

length = len(N)

def dfs(l, r, curr, tmp):
    if len(curr) == length:
        result.add(tmp)
    if l > 0:
        dfs(l - 1, r, N[l - 1:r], tmp + ''.join(N[l - 1:r]))
    if r < length:
        dfs(l, r + 1, N[l:r + 1], tmp + ''.join(N[l:r + 1]))

result = set()
for i in range(length):
    dfs(i, i, [], '')

print(len(result))