#이분탐색
#1개에 들어갈 수 있는 최대 강의 길이와, 각각이 들어갈 수 있는 시간을 최소로 하고
#갯수가 정해진것보다 초과하면 최소를 올리면서 진행해보자
N,M = map(int,input().split())

lessons = list(map(int,input().split()))

l = max(lessons)
r = sum(lessons)

m = (l+r)//2

ans = r

def is_possible(sz):
    cnt=1
    bluray = 0
    for lesson in lessons:
        if bluray + lesson <=sz:
            bluray += lesson
        else:
            cnt += 1
            bluray = lesson

    return cnt <= M

while l <= r:
    if is_possible(m):
        ans = m
        r = m-1
    else:
        l = m+1

    m = (l+r) // 2

print(ans)