#필요한 함수
#1. 각 물고기 방향전환
#2. 상어의 모든 경우의 수(DFS?)
# 7 6 2 3 15 6 9 8
# 3 1 1 8 14 7 10 1
# 6 1 13 6 4 3 11 4
# 16 1 8 7 5 2 12 2

data = []
data = [[7,6,2,3,15,6,9,8],[3,1,1,8,14,7,10,1],[6,1,13,6,4,3,11,4],[16,1,8,7,5,2,12,2]]

arr_fish= [[None]*4 for _ in range(4)]
for i in range(4):
    data = list(map(int,input().split()))
    for j in range(4):
        arr_fish[i][j] = [data[j*2],data[j*2+1]-1]

start_x = 0
start_y = 0
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

#회전 함수
def lotating(direction):
    return (direction + 1) % 8


#작은 순서부터 물고기 찾기위해서 물고기 위치 반환
def find_fish(arr,fish_num):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == fish_num:
                return i, j

    return None


def change_location(fish,px,py):
    for i in range(1,17):
        location = find_fish(arr_fish,i)
        if location != None:
            x,y = location[0],location[1]
            new_x,new_y = chk_move_possible(x,y,px,py)
            arr_fish[x][y],arr_fish[new_x][new_y] = arr_fish[new_x][new_y],arr_fish[x][y]


#px,py는 상어의 위치이다
def chk_move_possible(x,y,px,py):
    direction = data[x][y][1]
    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx <0 or nx >= 4 or ny < 0 or ny >= 4 or (nx == px and ny == py):
        for i in range(8):
            new_direction = lotating(direction)
            nx = x + dx[new_direction]
            ny = y + dy[new_direction]
            if nx>=0 and nx < 4 and ny>=0 and ny<4:
                if nx != px and ny != py:
                    break
    else:
        return nx,ny

    return nx, ny


