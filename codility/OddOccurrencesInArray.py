'''A non-empty zero-indexed array A consisting of N 
integers is given. The array contains an odd number of 
elements, and each element of the array can be paired 
with another element that has the same value, 
except for one element that is left unpaired.

Write a function that returns the value of the unpaired
element.
'''

def solution(A):
    count = dict()
    for i in A:
        count[i] = count.get(i, 0) + 1
    for key in count:
        if count[key] % 2 != 0:
            return key