from collections import deque

n = 4
computers = [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque()
visited = [[0]*n for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(n):
        start_x = i
        start_y = j

        if visited[start_x][start_y] == 0 and computers[start_x][start_y] == 1:
            q.append([i, j])
            answer += 1

        while q:
            x, y = q.popleft()
            if visited[x][y] == 0:
                visited[x][y] = 1

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    else:
                        if visited[nx][ny] == 0 and computers[nx][ny] == 1:
                            q.append([nx, ny])


print(answer)

