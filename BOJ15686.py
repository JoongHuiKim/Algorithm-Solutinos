from itertools import combinations

N,M = map(int,input().split())
house,chicken = [],[]

for i in range(N):
    data = list(map(int,input().split()))

    for j in range(N):
        if data[j] == 1:
            house.append((i,j))
        elif data[j] == 2:
            chicken.append((i,j))

candidates = list(combinations(chicken,M))

def cal_distance(candidates):
    distance = 0

    for hx,hy in house:
        temp = 987654321
        for cx,cy in candidates:
            temp = min(temp,abs(hx-cx) + abs(cy-hy))
        distance += temp

    return distance

result = 987654321
for var in candidates:
    result = min(result,cal_distance(var))

print(result)
