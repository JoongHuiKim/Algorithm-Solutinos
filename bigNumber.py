def solution():
    result = 0
    count = 0

    count = (m//(k+1))*k
    count += m%(k+1)

    result += count*first_num
    result += (m-count) * second_num

    return (result)


# 전체 더해야 하는 숫자 갯수를 연속가능 수로 나눈다
# 나머지는 2번째 큰수만큼 더해준다

n,m,k = map(int,input().split()) #5 ex)n개숫자, 8번, 연속 2회일때
data = list(map(int,input().split()))

data.sort()
first_num = data[n-1]
second_num = data[n-2]

print(solution())