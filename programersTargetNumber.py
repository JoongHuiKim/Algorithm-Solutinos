
def dfs(index,sum):
    global answer
    if len(numbers) == index:
        if sum == target:
            answer += 1

        return

    sum1 = sum + numbers[index]
    dfs((index + 1),sum1)
    sum2 = sum - numbers[index]
    dfs(index + 1,sum2)

    return answer


numbers = list(map(int,input().split(',')))
target = int(input())
answer = 0
dfs(0,0)
print(answer)
