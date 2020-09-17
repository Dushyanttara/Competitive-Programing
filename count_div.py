def solution(A, B, K):
    # write your code in Python 3.6
    q1 = A // K
    q2 = B // K
    rem_A = A % K
    if rem_A == 0:
        num_ints = q2 - q1 + 1
    else:
        num_ints = q2-q1
    return num_ints