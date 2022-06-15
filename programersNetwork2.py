from collections import deque

n = 3
# computers = [[1,1,0,1],[1,1,0,0],[0,0,1,1],[1,0,1,1]]
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
q = deque()
visited = [0]*n
answer = 0
for i in range(n):
    if computers[i][i] == 1 and visited[i] == 0:
        answer += 1
        visited[i] = 1
        for j in range(n):
            if computers[i][j] == 1 and visited[j] == 0:
                q.append(j)
                while q:
                    x = q.popleft()
                    visited[x] = 1
                    for k in range(n):
                        if computers[x][k] == 1 and visited[k] == 0:
                            q.append(k)

print(answer)