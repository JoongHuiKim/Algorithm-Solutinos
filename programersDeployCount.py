from collections import deque

progresses = list(map(int,input().split(',')))
speeds = list(map(int,input().split(',')))
answer = []
q1 = deque(progresses)
q2 = deque(speeds)

while q1:
    counter = 0
    for i in range(len(q1)):
        if q1[i] >= 100:
            continue
        else:
            q1[i] = q1[i] + q2[i]
            if q1[i] >= 100:
                q1[i] = 100

    if q1[0] == 100:
        for j in range(len(q1)):
            if q1[0] == 100:
                q1.popleft()
                q2.popleft()
                counter += 1

        answer.append(counter)

    if len(q1) == 1:
        answer.append(1)
        break

print(answer)