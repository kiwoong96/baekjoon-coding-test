import sys
input = sys.stdin.readline
INF = sys.maxsize

T = int(input())
k = 0
coins = [1, 10, 25]

dp = [INF for _ in range(100)]
dp[0] = 0
for coin in coins:
    for i in range(coin,100):
        dp[i] = min(dp[i],dp[i-coin]+1)
        
def solution(price):
    ans = 0
    while price:
        ans += dp[price % 100]
        price //= 100
    return ans

while T:
    T -= 1
    price = int(input())
    answer = solution(price)
    print(answer)