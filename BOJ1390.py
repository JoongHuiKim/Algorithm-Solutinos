from collections import deque
import sys
sys.setrecursionlimit(10**5)


def move(p_direction):
    global counter
    direction = p_direction
    x,y = queue[-1]
    if direction == "R":
        nx = x
        ny = y+1
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            counter += 1
            return
        for q in queue:
            if q[0] == nx and q[1] == ny:
                counter += 1
                return

        if data[nx][ny] == 2:
            queue.append([nx,ny])
            data[nx][ny] = 0
        else:
            queue.append([nx, ny])
            queue.popleft()
        counter += 1

        if D.get(counter) is not None:
            temp_direction = set_direction(direction,counter)
            direction = temp_direction
            move(direction)
        else:
            move(direction)
    elif direction == "L":
        nx = x
        ny = y-1
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            counter += 1
            return

        for q in queue:
            if q[0] == nx and q[1] == ny:
                counter += 1
                return

        if data[nx][ny] == 2:
            queue.append([nx,ny])
            data[nx][ny] = 0
        else:
            queue.append([nx, ny])
            queue.popleft()
        counter += 1

        if D.get(counter) is not None:
            temp_direction = set_direction(direction,counter)
            direction = temp_direction
            move(direction)
        else:
            move(direction)
    elif direction == "U":
        nx = x-1
        ny = y
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            counter += 1
            return

        for q in queue:
            if q[0] == nx and q[1] == ny:
                counter += 1
                return

        if data[nx][ny] == 2:
            queue.append([nx,ny])
            data[nx][ny] = 0
        else:
            queue.append([nx, ny])
            queue.popleft()
        counter += 1

        if D.get(counter) is not None:
            temp_direction = set_direction(direction,counter)
            direction = temp_direction
            move(direction)
        else:
            move(direction)
    elif direction == "D":
        nx = x+1
        ny = y
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            counter += 1
            return

        for q in queue:
            if q[0] == nx and q[1] == ny:
                counter += 1
                return

        if data[nx][ny] == 2:
            queue.append([nx,ny])
            data[nx][ny] = 0
        else:
            queue.append([nx, ny])
            queue.popleft()
        counter += 1

        if D.get(counter) is not None:
            temp_direction = set_direction(direction,counter)
            direction = temp_direction
            move(direction)
        else:
            move(direction)

    return


def set_direction(ori_direction,p_counter):
    new_direction = ''

    if ori_direction == "R":
        if D.get(p_counter) == "D":
            new_direction = "D"
        else:
            new_direction = "U"
    elif ori_direction == "L":
        if D.get(p_counter) == "D":
            new_direction = "U"
        else:
            new_direction = "D"
    elif ori_direction == "U":
        if D.get(p_counter) == "D":
            new_direction = "R"
        else:
            new_direction = "L"
    elif ori_direction == "D":
        if D.get(p_counter) == "D":
            new_direction = "L"
        else:
            new_direction = "R"

    return new_direction


N = int(input()) #N*N 크기
K = int(input()) #사과 갯수
apple = []
for i in range(K):
    apple.append(list(map(int,input().split())))

L = int(input()) #이동횟수
D = {}
queue = deque([])

for i in range(L):
    a,b = input().split()
    a = int(a)
    D[a] = b

data = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        data[i].append(0)

for var in apple:
    data[var[0]-1][var[1]-1] = 2

queue.append([0,0])
counter = 0
move('R')
print(counter)