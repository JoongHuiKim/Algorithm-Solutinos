import copy

data = []
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


def change_location(array,px,py):
    for i in range(1,17):
        location = find_fish(array,i)
        if location != None:
            x,y = location[0],location[1]
            direction = array[x][y][1]
            new_x,new_y,new_direction = chk_move_possible(x,y,px,py,direction)
            array[x][y][1] = new_direction
            array[x][y],array[new_x][new_y] = array[new_x][new_y],array[x][y]


#px,py는 상어의 위치이다
def chk_move_possible(x,y,px,py,direction):
    for i in range(8):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx >= 0 and nx < 4 and ny >= 0 and ny < 4:
            if not (nx == px and ny == py):
                direction = direction
                break
        direction = lotating(direction)

    return nx, ny, direction


def eat_possible(arr, now_x, now_y):
    positions = []
    direction = arr[now_x][now_y][1]

    for i in range(4):
        now_x = now_x + dx[direction]
        now_y = now_y + dy[direction]

        if now_x >= 0 and now_x < 4 and now_y >= 0 and now_y < 4:
            if arr[now_x][now_y][0] != -1:
                positions.append((now_x,now_y))
    return positions


def dfs(arr,now_x,now_y,total):
    global result
    array = copy.deepcopy(arr)
    total += array[now_x][now_y][0]
    array[now_x][now_y][0] = -1

    change_location(array,now_x,now_y)

    positions = eat_possible(array, now_x, now_y)

    if len(positions) == 0:
        result = max(result,total)
        return

    for nx,ny in positions:
        dfs(array,nx,ny,total)


result = 0
dfs(arr_fish,0,0,0)
print(result)