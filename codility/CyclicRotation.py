def solution(A, K):
    '''
    Rotate an array to the right by a given number of steps
    '''
    l = [] + A
    for i in A:
        try:
            l[K + A.index(i)] = i 
        except IndexError:
            l[K + A.index(i) - len(A)] = i   
    return l
    