#DFS
import sys
sys.setrecursionlimit(10**6)
def dfs(x1,x2):
    if x1 < 0 or x1>=r or x2<0 or x2>=c:
        return False

    if graph[x1][x2] == 1:
        graph[x1][x2] = 0
        dfs(x1,x2-1)
        dfs(x1,x2+1)
        dfs(x1-1,x2)
        dfs(x1+1,x2)

        return True
    return False


caseNum = int(input())

for num in range(caseNum):
    c, r, k = map(int, sys.stdin.readline().split())
    data = []

    for i in range(k):
        data.append(list(map(int, input().split())))
        #data.append(list(map(int, sys.stdin.readline().split())))

    graph = []
    zero = []
    count = 0

    for x in range(r):
        for y in range(c):
            zero.append(0)
        graph.append(zero)
        zero = []

    for a in data:
        graph[a[1]][a[0]] = 1

    for i in range(r):
        for k in range(c):
            if dfs(i, k) == True:
                count += 1

    print(count)
