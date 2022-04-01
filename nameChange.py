#아이디 변환하기
def solution(new_id):
    lowerId = new_id.lower()
    filter = '~!@#$%^&*()=+[{]}:?,<>/'
    answer = ''

    for letter in lowerId:
        if letter in filter:
            continue
        else:
            answer += letter

    for i in range(len(answer)):
        answer = answer.replace("..",".")

    if answer[0] == ".":
        answer = answer[1:]
        if answer == '':
            answer = 'a'

    if answer[len(answer)-1] == ".":
        answer = answer[:-1]

    if answer == "":
        answer = "a"
    if len(answer) >= 16:
        answer = answer[:15]
        while True:
            if answer[len(answer) - 1] == ".":
                answer = answer[:-1]
            else:
                break


    if len(answer)<=2:
        while len(answer) <=2:
            answer += answer[len(answer)-1]

    return answer


print(solution("=.="))