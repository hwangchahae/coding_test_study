#메모리: 40224KB, 시간: 456ms



X = int(input())


#DP = 계산 카운트
DP = [0] * (X+1)


for i in range(2, X+1):
    DP[i] = DP[i-1] + 1
    if i % 2 == 0:
        DP[i] = min(DP[i], DP[i // 2] + 1)
    if i % 3 == 0:
        DP[i] = min(DP[i], DP[i // 3] + 1)


print(DP[X])
