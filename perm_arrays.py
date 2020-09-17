def solution(A):
    # write your code in Python 3.6
    max_val = max(A)
    perm_sum = max_val *(max_val+1)//2
    total_sum = sum(A)
    set_A = set(A)
    if (total_sum == perm_sum ) and (len(set_A) == len(A)) :
        return 1
    else:
        return 0