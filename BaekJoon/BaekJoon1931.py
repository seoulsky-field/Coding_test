import sys
input = sys.stdin.readline

N = int(input())
times = list(tuple(map(int, input().split())) for _ in range(N))
times = sorted(times, key=lambda x: (x[1], x[0]))

count, end_time = 0, 0
for (start, end) in times:
    if start >= end_time:
        count += 1
        end_time = end

print(count)

# N = int(input())
# times = dict()
# count = 0

# for _ in range(N):
#     start, end = map(int, input().split())
#     try:
#         times[start].append(end)
#     except:
#         times[start] = [end]

# times = sorted(times.items(), key = lambda item: item[1])

# end_time = 0
# for time_set in times:
#     if time_set[0] >= end_time:
#         # print(time_set)
#         count += 1
#         end_time = sorted(time_set[1])[0]

# print(count)