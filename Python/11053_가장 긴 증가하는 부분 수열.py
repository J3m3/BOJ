input = __import__("sys").stdin.readline

N = int(input())
arr = [*map(int, input().split())]

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))
