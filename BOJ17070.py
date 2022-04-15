#갈수있는 방향 0,1  1,1  1,0 3개만 가능
#이동할때마다 이전행의 +1해서 N,M이 0이 아니면 그 값

N = int(input())
data = []
answer = 0
for i in range(N):
    data.append(list(map(int,input().split())))


def dfs(direction,x,y):
    global answer

    if x<0 or x>=N or y<0 or y>=N:
        return
    else:
        if x==N-1 and y==N-1:
            answer += 1

        else:
            if direction == "R":
                if data[x][y] == 1:
                    return
                dfs("R", x , y + 1)
                dfs("RD", x + 1, y + 1)
            elif direction == "RD":
                if data[x-1][y] == 1 or data[x][y] == 1 or data[x][y-1] == 1:
                    return
                dfs("R", x , y + 1)
                dfs("RD",x + 1, y + 1 )
                dfs("D",x+1,y)
            elif direction == "D":
                if data[x][y] == 1:
                    return
                dfs("RD",x + 1, y + 1 )
                dfs("D",x+1,y)


dfs("R",0,1)
print(answer)

# /*
#
# 6
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 1 0
# 0 0 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 1 0
# correct: 1
# wrong: 0
#
# 6
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 1 0
# 0 0 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# correct: 5
# wrong: 4
#
# 6
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 1 0
# 0 0 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 1 0 0
# correct: 3
# wrong: 2
#
# 7
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 1 0 0 0 1 0
# 0 0 0 0 0 0 0
# 1 0 0 0 1 1 0
# 0 0 0 0 0 0 0
# 0 1 0 0 0 0 0
# correct: 9
# wrong: 8
#
# 7
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 1 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# correct: 53
# wrong: 52
#
# 16
# 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
# 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 1 0 0 0 0 1 0 0 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 0
# 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 1 0 0 0 1 0 0 0 1 0 1 0 0
# 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
# 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 1
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# correct: 109
# wrong: 103
# */