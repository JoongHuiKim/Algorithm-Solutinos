from collections import deque

s = input()
answer = -1
list_N = list(s)
q = deque(list_N)
stack = []
stack.append(q.popleft())
while True:

    if not q:
        break
    else:
        if not stack:
            stack.append(q.popleft())
        if not q:
            break

        if stack[-1] == q[0]:
            stack.pop()
            q.popleft()
        else:
            stack.append(q.popleft())


if not stack:
    answer = 1
else:
    answer = 0


print(answer)
