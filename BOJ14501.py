def solution(index):
    global sumVal

    if index == N-1:
        if data[index][0] == 1:
            sumVal += data[index][1]
            return True
        else:
            return True

    temp_index = index + data[index][0]
    if temp_index >= N:
        return True
    else:
        sumVal += data[index][1]
        solution(temp_index)

    return True


N = int(input())
sumVal = 0
data = []
val = []
for i in range(N):
    data.append(list(map(int,input().split())))


for i in range(N):
    sumVal = 0
    solution(i)
    val.append(sumVal)

print(max(val))