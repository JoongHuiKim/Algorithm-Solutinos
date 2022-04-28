#필요한 함수
#1. 각 물고기 방향전환
#2. 상어의 모든 경우의 수
# 7 6 2 3 15 6 9 8
# 3 1 1 8 14 7 10 1
# 6 1 13 6 4 3 11 4
# 16 1 8 7 5 2 12 2

data = []
data = [[7,6,2,3,15,6,9,8],[3,1,1,8,14,7,10,1],[6,1,13,6,4,3,11,4],[16,1,8,7,5,2,12,2]]

fish= [[None]*4 for _ in range(4)]
for i in range(4):
    data = list(map(int,input().split()))
    for j in range(4):
        fish[i][j] = [data[j*2],data[j*2+1]-1]

start_x = 0
start_y = 0
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def change():
    fish[start_x][start_y] = 0
