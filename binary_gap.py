def dec_to_bin(N):
    return str(bin(N).replace("0b",""))
    
    
def solution(N):
    # write your code in Python 3.6
    bin_N = dec_to_bin(N)
    ind_1 = []
    for i in range(len(bin_N)):
        if i - int(bin_N[i]) != i:
            ind_1.append(i)
    bin_gap = 0
    for j in range(len(ind_1)-1):
        gap = ind_1[j+1] - ind_1[j]-1
        if bin_gap < gap:
            bin_gap = gap
            
    return bin_gap


p = 32
answer = solution(p)
sample_list = [1,2,3,4,54,5,5,5,55,5,56,6,67]
print(sample_list[-1])