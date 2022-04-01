#DFS
def dfs(r,c):
    if r < 0 or r>=N or c<0 or c>=N:
        return False

    global count
    if data[r][c] == 1:
        data[r][c] = 0

        count += 1
        dfs(r,c-1)
        dfs(r,c+1)
        dfs(r-1,c)
        dfs(r+1,c)
        return True
    return False


N = int(input())
data = []
count = 0
num = []
for i in range(N):
    data.append(list(map(int,input())))

for i in range(N):
    for j in range(N):
        if dfs(i,j) == True:
            num.append(count)
            count = 0

num.sort()
print(len(num))
for x in num:
    print(x)