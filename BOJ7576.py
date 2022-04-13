from collections import deque

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=r or ny <0 or ny>=c:
                continue
            else:
                if data[nx][ny] == 0:
                    data[nx][ny] = data[x][y] + 1
                    queue.append([nx, ny])



c,r = map(int,input().split())
data =[]
queue = deque([])

for i in range(r):
    data.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer = 0

for i in range(r):
    for j in range(c):
        if data[i][j] == 1:
            queue.append([i,j])

bfs()

for i in range(r):
    for j in range(c):
        if data[i][j] == 0:
            answer = -1
            break

if answer != -1:
    #중요! 이차원 리스트에서 바로 max를 써버리면 합이 최대인 row가 튀어나오니 map(max,data)를 써서
    #row별 최대값을 가져오고 그 다음에 max를 다시하자
    answer = max(map(max,data))
    #temp = 0
    #for i in range(r):
    #    answer = max(max(data[i]),temp)
    answer -= 1

print(answer)