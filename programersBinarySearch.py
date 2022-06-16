n= 6
times = [7,10]
answer = 0
max_time = max(times)*n
min_time = 1

while min_time <= max_time:
    mid_time = (min_time + max_time)//2
    temp = 0

    for time in times:
        temp += mid_time//time
        if temp >=n:
            break

    if temp >= n:
        answer = mid_time
        max_time = mid_time -1

    elif temp<n:
        min_time = mid_time +1


print(answer)