def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')

    for i in graph[v]:
        if not visited[i]==True:
            dfs(graph,i,visited)

def bfs(graph,v,visited):
    visited[v] = True
    queue = deque([v])
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)



from collections import deque

x,y,z = map(int,input().split())

graph = []
visited = [False]*(x+1)
graph = [[] for _ in range(x+1)]

for _ in range(y):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,x+1):
    graph[i].sort()

dfs(graph,z,visited)

visited = [False]*(x+1)
print()
bfs(graph,z,visited)