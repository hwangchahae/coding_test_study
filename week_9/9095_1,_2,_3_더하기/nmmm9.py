# 32412	48ms

t = int(input())
dp = [0] * 12  # 최대 n=11
dp[1] = 1  # 1
dp[2] = 2  # 1+1, 2
dp[3] = 4  # 1+1+1, 1+2, 2+1, 3

for i in range(4, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(t):
    n = int(input())
    print(dp[n])
