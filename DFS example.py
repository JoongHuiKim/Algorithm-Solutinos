def dfs(x,y):
    if x < 0 or x >=n or y < 0 or y>=m: #행렬의 범위가 넘어서는 경우 전부 제외한다
        return False

    if graph[x][y] == 0:
        print(graph[x][y])
        graph[x][y] = 1 #방문했으면 1로 한다.

        #가장처음 1,1 기준으로 상하좌우 전부 한번 따져본다.
        #재귀함수 호출이므로 아래 4가지 경우 중 한번이라도 이동에 성공하면 그 위치에서 또 상하좌우를 찾는다
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

#행렬의 형태를 받는다
n,m = map(int,input().split())

#이차원 리스트 -> 행렬의 형태를 띈다
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

result = 0
#행렬시작점을 전부다 한번씩 해보자
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)