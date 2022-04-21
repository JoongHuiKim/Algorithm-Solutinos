import math

N = int(input())
room = list(map(int,input().split()))
b,c = map(int,input().split())
counter = 0
for num in room:
    num = num - b
    if (num <0):
        num = 0
    counter += math.ceil(num/c)

answer = counter + N
print(answer)