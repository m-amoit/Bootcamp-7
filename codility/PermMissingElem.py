def solution(A):
    N = len (A) 
    # Sum of elements in an arithmetic progression
    total = ((N+1)*(N+2))/2
    # Subtract to find missing element
    for i in A:
        total -= i
    return total
    