def solution(S, P, Q):
    # write your code in Python 3.6
    nuc_score = {"A":1,
                "C" :2,
                "G" :3,
                "T" :4,
                }
    s_new = []
    for nuc in S:
        s_new.append(nuc_score[nuc])  
    
    answers = []
    for k in range(len(P)):
        left_bound = P[k]
        right_bound = Q[k]
        
        nuc_slice = s_new[left_bound:right_bound+1]
        answer = min(nuc_slice)
        answers.append(answer)
    return answers
    