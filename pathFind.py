#시작은 1,1이고 이동 계획이 주어졌을 때 최종 좌표는?
#입력1 횟수, 입력2 이동 방법 L, R, U , D
x,y = 1,1

N = int(input())
move = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_plan = ['L', 'R', 'U', 'D']

for element in move:
    for i in range(len(move_plan)):
        if element == move_plan[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx<1 or nx>N or ny<1 or ny>N:
        continue
    x,y = nx,ny

print(x,y)
