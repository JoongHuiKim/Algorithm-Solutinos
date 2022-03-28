def bfs(x,y):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>= r or ny<0 or ny>=c:
                continue

            if data[nx][ny] == 0:
                continue
            if data[nx][ny] == 1:
                data[nx][ny] = data[x][y] + 1
                queue.append((nx,ny))
    return data[r-1][c-1]

from collections import deque
import sys
#항상 실제로는 sys.stdin.readline()이 더 빠르다
#또한 맨 마지막에 개행문자가 디폴트로 들어가서 strip를 꼭 쓰자
r,c = map(int,input().split())
#r,c = map(int,sys.stdin.readline().split())

data = []

for i in range(r):
    data.append(list(map(int,input())))
    #data.append(list(map(int,sys.stdin.readline().strip())))

#이동방법
dx = [0,0,-1,1]
dy = [-1,1,0,0]

x,y = 0,0

queue = deque()
queue.append((x,y))

print(bfs(x,y))