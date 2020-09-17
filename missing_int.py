def solution(A):
    # write your code in Python 3.6
    max_val = max(A)
    
    if max_val > 1:
        for i in range(1,max_val+2):
                if i not in A:
                    return i
            
    else:
        result = int(1)
        return result

def solution(A):
    max_val = max(A)
    active = True
    i = 0
    if max_val >0:
        while active:
            if i not in A:
                return i
                active = False
            else:
                i++
    else:
        return 1    


