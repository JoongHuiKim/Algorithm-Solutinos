N = int(input())
data = list(map(int,input().split()))

add,sub,mul,div = map(int,input().split())
min_val = 987654321
max_val = -987654321

def dfs(i,now):
    global min_val, max_val,add,sub,mul,div
    if i == N:
        min_val = min(now,min_val)
        max_val = max(now,max_val)

    if add>0:
        add -= 1
        dfs(i+1,now + data[i])
        add += 1
    if sub>0:
        sub -= 1
        dfs(i+1,now - data[i])
        sub += 1
    if mul>0:
        mul -= 1
        dfs(i+1,now * data[i])
        mul += 1
    if div>0:
        div -= 1
        dfs(i+1,int(now/data[i]))
        div += 1


dfs(1,data[0])
print(max_val,min_val)
