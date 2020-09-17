def frog_jump(S, k, q):
    n = len(S)
    dp = [1] + [0] * k
    for i in range(1,k+1):
        for j in range(n):
            dp[i] = (dp[i] + dp[i-S[j]] ) % q
    return dp[k] 

distance_list = [1,2,3,5,6,7,8]

k = 25
q = 10

answer = frog_jump(distance_list, k, q)
print(answer)