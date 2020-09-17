def prefix_sum(A):
    N = len(A)
    P = [0] * (N + 1)
    for k in range(1,N+1):
        P[k] = P[k-1] + A[k-1]
    return P
    
def slice_avg(P,x,y):
    total_sum = P[y] - P[x]
    avg_slice = (total_sum) / (y-x)
    return avg_slice
    
def solution(A):
    # write your code in Python 3.6
    pref = prefix_sum(A)
    N = len(A)
    avg_slice = 10e9
    final_p = 0
    for p in range(len(A)-1):
        for q in range(p+1,len(A)):
            curr_avg = slice_avg(pref,p, q+1)
            curr_slice = A[p:q+1]
            if len(curr_slice) < N:
                print("p:",p)
                print("q:",q)
                print("avg_slice: ",avg_slice)
                print("slice:",curr_slice)
                print("curr_avg:",curr_avg)
                if curr_avg < avg_slice:
                    avg_slice = curr_avg
                    final_p = p
                    print("final_p:",p)
                print("===============")
               
    return final_p

def solution(A):
    # write your code in Python 3.6
    pref = prefix_sum(A)
    N = len(A)
    avg_slice = 10e9
    final_p = 0
    for p in range(len(A)-1):
        for q in range(p+1,len(A)):
            curr_avg = slice_avg(pref,p, q+1)
            curr_slice = A[p:q+1]
            #if len(curr_slice) < N:
            print("p:",p)
            print("q:",q)
            print("avg_slice: ",avg_slice)
            print("slice:",curr_slice)
            print("curr_avg:",curr_avg)
            if curr_avg < avg_slice:
                avg_slice = curr_avg
                final_p = p
                print("final_p:",p)
            print("===============")
               
    return final_p

sample_array =  [5, 6, 3, 4, 9]
sample_array = [-3, -5, -8, -4, -10]
print(sample_array)
answer  = solution(sample_array)
print(answer)


