import heapq

scoville = list(map(int,input().split(',')))
K = int(input())

heapq.heapify(scoville)
min_value1 = 0
answer = 0
while True:
    min_value1 = heapq.heappop(scoville)
    if min_value1 >= K:
        break
    else:
        if len(scoville) == 0:
            answer = -1
            break
        else:
            min_value2 = heapq.heappop(scoville)

            new_num = min_value1 + (min_value2 * 2)
            heapq.heappush(scoville, new_num)
            answer += 1


print(answer)
