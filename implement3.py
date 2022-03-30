#프로그래머스 로또번호로 등수 맞추기
def solution(lottos,win_nums):
    answer = []
    maxN = 0
    minN = 0

    variable = 0
    for i in lottos:
        if i == 0:
            variable += 1

    for k in lottos:
        for x in win_nums:
            if k==x:
                minN += 1

    if variable > 0:
        maxN = minN + variable
    else:
        maxN = minN

    temp = []
    temp.append(maxN)
    temp.append(minN)

    for num in temp:
        if num == 6:
            answer.append(1)
        elif num == 5:
            answer.append(2)
        elif num == 4:
            answer.append(3)
        elif num == 3:
            answer.append(4)
        elif num == 2:
            answer.append(5)
        elif num <=1:
            answer.append(6)

    return answer

l = list(map(int,input().split(', ')))
w = list(map(int,input().split(', ')))

print(solution(l,w))