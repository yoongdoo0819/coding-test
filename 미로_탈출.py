# 미로 탈출

from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        if x == n-1 and y == m-1:
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] += graph[x][y]
                queue.append((nx, ny))
            
bfs(0, 0)
print(graph[n-1][m-1])