## 메모리 : 40224 KB, 시간 : 456 ms
import sys

N = int(sys.stdin.readline())

dp = [0] * (N + 1)

if N >= 1 :
    dp[1] = 0
if N >= 2 : 
    dp[2] = 1
if N >= 3 :
    dp[3] = 1

if N >= 4 :
    for i in range(4, N + 1) :
        dp[i] = dp[i-1] + 1  
        
        if i % 2 == 0 :
            dp[i] = min(dp[i], dp[i//2] + 1)
        
        if i % 3 == 0 :
            dp[i] = min(dp[i], dp[i//3] + 1)
    
print(dp[N])