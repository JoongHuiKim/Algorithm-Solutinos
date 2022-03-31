#카카오 오픈채팅방 문제 레벨2
def solution(record):
    answer = []
    id_nick_dict = {}

    for i in record:
        i = i.strip("\"")
        a = list(map(str,i.split()))

        if len(a) == 3:
            id_nick_dict[a[1]] = a[2]

    for i in record:
        i = i.replace("\"","")
        i = i.strip()
        a = list(map(str, i.split()))
        msg = ''
        tempNick = ''
        tempNick = id_nick_dict[a[1]]


        msg = tempNick + "님이"
        if a[0] == 'Enter':
            msg = msg + " " + "들어왔습니다."
        elif a[0] == 'Leave':
            msg = msg + " " + "나갔습니다."
        else:
            continue

        answer.append(msg)
    return answer


x=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(x))