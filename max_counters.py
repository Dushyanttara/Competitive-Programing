def increase(X,counters):
    counters[X] += 1
    return counters
    
def max_counter(counters):
    max_val = max(counters)
    counters = [max_val]*len(counters)
    return counters
    
def solution(N, A):
    # write your code in Python 3.6
    counters = [0 for _ in range(N)]
    
    for op in A:
        if op < N+1:
            counters = increase(op-1,counters)
        else :
            counters = max_counter(counters)
    return counters