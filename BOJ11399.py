#그리디
def solution():
    answer = 0
    temp = 0
    for i in range(N):

        if (i == 0):
            temp = arr[i]
            answer += temp
        else:
            temp = (temp + arr[i])
            answer += temp

    return answer


N = int(input())

arr = list(map(int, input().split()))
arr.sort()
print(solution())