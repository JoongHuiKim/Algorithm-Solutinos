from collections import deque
import sys

#1. 최소의 경로를 먼저 구해보자
def bfs():
    dist = [[-1] * N for _ in range(N)]
    queue.append([start_x,start_y])
    dist[start_x][start_y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            else:
                if dist[nx][ny] == -1 and data[nx][ny] <= shark_size:
                    queue.append([nx, ny])
                    dist[nx][ny] = dist[x][y] + 1

    return dist


def find(dist):
    x,y = 0,0
    min_value = INF
    for i in range(N):
        for j in range(N):
            if dist[i][j] != -1 and 1 <= data[i][j] < shark_size:
                if dist[i][j] < min_value:
                    x = i
                    y = j
                    min_value = dist[i][j]

    if min_value == INF:
        return None
    else:
        return x,y,min_value


N = N = int(input())
#N = int(sys.stdin.readline().strip())

data = []
for i in range(N):
    data.append(list(map(int, input().split())))
    #data.append(list(map(int,sys.stdin.readline().split())))

INF = 987654321
start_x,start_y = (0,0)
for i in range(N):
    for j in range(N):
        if data[i][j] == 9:
            start_x = i
            start_y = j

data[start_x][start_y] = 0
queue = deque([])
dx = [-1,0,1,0]
dy = [0,-1,0,1]

shark_size = 2
eat_fish = 0
answer = 0

while True:
    value = find(bfs())

    if value == None:
        print(answer)
        break
    else:
        answer += value[2]
        start_x = value[0]
        start_y = value[1]
        data[start_x][start_y] = 0

        eat_fish += 1
        if eat_fish == shark_size:
            shark_size += 1
            eat_fish = 0
