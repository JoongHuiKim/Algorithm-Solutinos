n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
location_table = {}
cur = k
answer = ['O']*n
stack = []

for i in range(n):
    location_table[i] = []

location_table[0] = [None,1]

for i in range(1,n-1):
    location_table[i] = [i-1,i+1]

location_table[n-1] = [n-2,None]

for handle in cmd:
    if handle == 'C':
        answer[cur] = 'X'
        pre,next = location_table[cur]
        #커서 정보 저장
        stack.append([pre,cur,next])

        #커서를 이동
        #만약에 뒤에 있는행이였으면 그 이전행을 선택한다
        if next == None:
            cur = location_table[cur][0]
        else:
            cur = location_table[cur][1]

        if pre == None:
            location_table[next][0] = None
        elif next == None:
            location_table[pre][1] = None
        else:
            location_table[pre][1] = next
            location_table[next][0] = pre

    elif handle == 'Z':
        pre,loc,next = stack.pop()
        answer[loc] = 'O'
        if pre == None:
            location_table[next][0] = loc
        elif next == None:
            location_table[pre][1] = loc
        else:
            location_table[pre][1] = loc
            location_table[next][0] = loc

    else:
        x1,x2 = handle.split()
        x2 = int(x2)
        if x1 == 'D':
            for j in range(x2):
                cur = location_table[cur][1]
        elif x1 == 'U':
            for j in range(x2):
                cur = location_table[cur][0]


answer = ''.join(answer)
print(answer)