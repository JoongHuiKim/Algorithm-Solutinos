from collections import deque
import copy

def set_wall(param,param1):

    for i in range(len(param)):
        x1, x2, x3 = 0,0,0
        y1, y2, y3 = 0,0,0
        x1,y1 = param[i]
        for j in range(i+1,len(param)):
            x2,y2 = param[j]
            for k in range(j+1,len(param)):
                x3,y3 = param[k]
                param1[x1][y1] = 1
                param1[x2][y2] = 1
                param1[x3][y3] = 1
                bfs(param1)
                param1 = []
                param1 = copy.deepcopy(data)



def bfs(param2):
    queue = deque([])
    for i in range(R):
        for j in range(C):
            if param2[i][j] == 2:
                queue.append([i,j])

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            else:
                if param2[nx][ny] == 0:
                    param2[nx][ny] = 2
                    queue.append([nx, ny])

    counter = 0
    for i in range(R):
        for j in range(C):
            if param2[i][j] == 0:
                counter += 1

    answer.append(counter)


R,C = map(int,input().split())
data = []
c_data = []
zeros = []
answer = []

dx = [0,0,-1,1]
dy = [-1,1,0,0]

for i in range(R):
    data.append(list(map(int,input().split())))

for i in range(R):
    for j in range(C):
        if data[i][j] == 0:
            zeros.append([i,j])

c_data = copy.deepcopy(data)
set_wall(zeros,c_data)
print(max(answer))