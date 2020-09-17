def solution(X, A):
    # write your code in Python 3.6
    loc_array = [0 for _ in range(X)]
    print(loc_array)
    for time in range(len(A)):
        loc_array[A[time]-1] +=1
        print(loc_array)
        if 0 not in loc_array:
            return time
    
    if 0 in loc_array:
        return -1
