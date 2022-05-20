import copy


def first(que,w):
    global c_matrix
    temp = []
    for i in range(w):
        c_matrix[que[0]][que[1]+i+1] = matrix[que[0]][que[1]+i]
        temp.append(matrix[que[0]][que[1]+i])

    return min(temp)


def second(que,w,h):
    global c_matrix
    temp = []
    for i in range(h):
        c_matrix[que[0]+i+1][que[1]+w] = matrix[que[0]+i][que[1]+w]
        temp.append(matrix[que[0]+i][que[1]+w])

    return min(temp)


def third(que,w):
    global c_matrix
    temp = []
    for i in range(w):
        c_matrix[que[2]][que[3]-i-1] = matrix[que[2]][que[3]-i]
        temp.append(matrix[que[2]][que[3]-i])

    return min(temp)


def forth(que,w,h):
    global c_matrix
    temp = []
    for i in range(h):
        c_matrix[que[2]-i-1][que[3]-w] = matrix[que[2]-i][que[3]-w]
        temp.append(matrix[que[2]-i][que[3]-w])

    return min(temp)


r = int(input())
c = int(input())

# queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
# queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
queries = [[1,1,100,97]]
len_queries = len(queries)
for i in range(len_queries):
    for j in range(len(queries[0])):
        queries[i][j] = queries[i][j] - 1

matrix = [[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        matrix[i][j] = (c*i) + (j+1)

c_matrix = copy.deepcopy(matrix)
answer = []
for k in range(len_queries):
    height = queries[k][2] - queries[k][0]
    width = queries[k][3] - queries[k][1]

    num1 = first(queries[k],width)
    num2 = second(queries[k],width,height)
    num3 = third(queries[k],width)
    num4 = forth(queries[k],width,height)

    answer.append(min(num1,num2,num3,num4))
    matrix = copy.deepcopy(c_matrix)


print(answer)



