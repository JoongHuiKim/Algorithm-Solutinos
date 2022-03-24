# 다이나믹 프로그래밍
def solution(num):
    answer = 0
    if num == 4 or num == 7:
        answer = -1
        return answer

    if num % 5 == 0:
        answer = num//5
        return answer
    else:
        temp = num % 5

        if temp == 1:
            answer = num//5 + 1
        elif temp == 2:
            answer = num//5 + 2
        elif temp == 3:
            answer = num//5 + 1
        elif temp == 4:
            answer = num//5 + 2

    return answer


N = int(input())
print(solution(N))
