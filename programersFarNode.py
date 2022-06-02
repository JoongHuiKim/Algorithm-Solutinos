# [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
from collections import deque

def bfs(p_dist):
    while q:
        now = q.popleft()
        for nx in v[now]:
            if dist[nx] == -1:
                dist[nx] = dist[now] + 1
                q.append(nx)


edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

n = 6
v = [[] for _ in range(n+1)]
dist = [-1 for _ in range(n+1)]
q = deque([])

for num in edge:
    v[num[0]].append(num[1])
    v[num[1]].append(num[0])

for node in v:
    node.sort()

q.append(1)
dist[1] = 0
bfs(dist)

max_val = max(dist)
answer = 0
for i in range(len(dist)):
    if dist[i] == max_val:
        answer += 1

print(answer)


