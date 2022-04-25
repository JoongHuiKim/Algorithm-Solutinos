import sys
sys.setrecursionlimit(10**5)

def dfs(i,j,cnt,val):
    global answer1
    if cnt == 4:
        answer1 = max(answer1,val)
        return

    if i<0 or i>=R or j<0 or j>=C:
        return
    else:
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            else:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    dfs(nx, ny, cnt + 1, val+data[nx][ny])
                    visited[nx][ny] = False


def other(i,j):
    global answer2
    #ㅏ모양 체크
    if i+2 < R and j+1 < C:
        answer2 = max(answer2,data[i][j] + data[i+1][j] + data[i+2][j] + data[i+1][j+1])
    # ㅓ 모양 체크
    if i+2 < R and j-1 > 0:
        answer2 = max(answer2, data[i][j] + data[i + 1][j] + data[i + 2][j] + data[i + 1][j - 1])
    # ㅗ 모양 체크
    if i-1 > 0 and j+2 < C:
        answer2 = max(answer2, data[i][j] + data[i][j+1] + data[i][j+2] + data[i - 1][j + 1])
    # ㅜ 모양 체크
    if i+1 < R and j+2 < C:
        answer2 = max(answer2, data[i][j] + data[i][j + 1] + data[i][j + 2] + data[i + 1][j + 1])


R,C = map(int,input().split())
data = []
for i in range(R):
    data.append(list(map(int,input().split())))

visited = [[False]*C for _ in range(R)]
answer1 = 0
answer2 = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(R):
    for j in range(C):
        visited[i][j] = True
        dfs(i, j, 1, data[i][j])
        visited[i][j] = False

        other(i,j)


print(max(answer1,answer2))



