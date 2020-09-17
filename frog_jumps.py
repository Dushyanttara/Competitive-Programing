def solution(X, Y, D):
    # write your code in Python 3.6
    ideal_jumps = (Y-X)//D
    rem = (Y-X) % D
    if rem == 0:
        jumps = ideal_jumps
    else:
        jumps = ideal_jumps + 1
        
    return jumps

p = solution(5,200,10)

print(p)