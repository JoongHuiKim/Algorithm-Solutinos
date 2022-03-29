def solution(id_list, report, N):
    answer = [0]*len(id_list)
    reported_dict = {}
    for i in id_list:
        reported_dict[i] = 0

    unique_report = set(report)

    for k in unique_report:
        a,b = k.split()
        reported_dict[b] += 1

    for l in unique_report:
        a,b = l.split()
        if reported_dict.get(b) >= N:
            answer[id_list.index(a)] += 1

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
N = 2

solution(id_list,report,N)