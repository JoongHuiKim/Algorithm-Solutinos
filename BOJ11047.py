#그리디
def solution(inputArr):
    global money
    answer = 0

    for i in range(inputLen):
        if money // inputArr[i] > 0:
            count = (money // inputArr[i])
            answer += count
            money -= (inputArr[i] * count)

    return answer


inputLen, money = map(int, input().split())
inputArr = []

for i in range(inputLen):
    inputArr.append(int(input()))

inputArr.sort(reverse=True)
print(solution(inputArr))