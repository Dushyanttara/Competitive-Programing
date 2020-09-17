import sys

def dynamic_coin_changing(c,k):
    n = len(c)
    #create two dimensional array with all zeros
    dp = [[0] * (k+1) for i in range(n+1)]
    dp[0] = [0] + [sys.maxsize] * (k)

    for i in range(1, n+1):
        for j in range(c[i-1]):
            dp[i][j] = dp[i-1][j]
        for j in range(c[i-1],k+1):
            dp[i][j] = min(dp[i][j-c[i]], dp[i-1][j])
    return dp[n]

#Optimized memory usage
def dynamic_coin_changing(c,k):
    n = len(c)
    dp = [0] + [sys.maxsize] * (k)
    for i in range(1, n+1):
        for j in range(c[i-1], k+1):
            dp[j] = min(dp[j- c[i-1]] + 1, dp[j])
    return dp

denominations_list = [1,2,3,4,5,6,7,8,9,10,11,12]

final_value = 85

answer = dynamic_coin_changing(denominations_list, final_value)
print(answer)
