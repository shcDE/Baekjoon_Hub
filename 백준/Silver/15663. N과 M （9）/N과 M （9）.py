import sys

n, m = map(int, sys.stdin.readline().split())
n_list = sorted(list(map(int, sys.stdin.readline().split())))
visited = [0 for _ in range(n)]
total = []

def dfs():
    if len(total) == m:
        print(*total)
        return
    
    memorize = 0
    
    for i in range(n):
        if not visited[i] and memorize != n_list[i]:
            visited[i] = 1
            total.append(n_list[i])
            memorize = n_list[i]
            dfs()
            visited[i] = 0
            total.pop()
            
dfs()