def solution(n):
    answer = n // 7 + 1
    if n % 7 == 0:
        return n // 7
    return answer