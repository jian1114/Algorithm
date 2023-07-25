# 1789 수들의 합
S = int(input())
i = 1
cnt, sum = 0, 0
while sum <= S:
    sum += i
    cnt += 1
    i += 1
print(cnt - 1)