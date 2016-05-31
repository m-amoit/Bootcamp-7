def solution(A):
    total = A[0]
    y = sum(A)
    result = abs(2*total - y)
    for P in range(1, len(A)):
        total += A[P]
        diff = abs(2*total - y)
        result = min(diff, result)
    return result