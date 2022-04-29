# CMPS 2200 Assignment 5
## Answers

**Name:**____Maria Chen_____________________


Place all written answers from `assignment-05.md` here for easier grading.





- **1a.**
First find the smallest k that satisfies 2^k >= N. Then traverse from k to 0, and compare N with 2^i each time. If N>=2^i, then reduce N by 2^i and record 2^i, the answer is all coins recorded.
Proof of legitimacy: Any number can be represented in binary form, and all the coins of binary power in this problem exist, so N dollars can definitely be made up. At the same time, after arbitrarily selecting a legal conis, there must also be a legal scheme for the newly generated numbers. When greedy selection from large to small, if a certain amount of coins that can be collected is not selected, more coins need to be accumulated in order to collect the corresponding amount later. So the above greedy algorithm is correct.


- **1b.**
Work: O(logN).
Span: O(logN)
Start from 1 and find the smallest k to satisfy 2^k>=N, and the time overhead is O(logN). Then loop through k to 0 to select coins, the time overhead is O(logN), so the work is O(logN),span is O(logN)


- **2a.**
  Suppose there are a total of 3 coins, the denominations are {2, 6, 7}, and you need to find $8. According to the above algorithm, first select 7, then N becomes 1, and then it cannot be selected. But actually 2 and 6 should be chosen. The reason for the error of the greedy algorithm is that the greedy algorithm only considers the local optimal solution, and does not consider the optimal solution from the overall point of view. When 7 is found, 7 is directly selected, but because coins cannot be split and do not exist coins with a denomination of 1, so there is an error.

  
- **2b.**
def func(N, coins, cnt, ans, dp):
    if N == 0:
        if ans[0] > cnt:
            ans[0] = cnt
        return cnt
    if len(coins) == 0:
        return
    if dp[N][len(coins)] != 0:
        return dp[N][len(coins)]
    for i in range(N/coins[0]+1):
        value = func(N-i*coins[0], coins[1:], cnt + i, ans, dp)
        if value is None:
            if dp[N][len(coins)] == 0 or dp[N][len(coins)] is None:
                dp[N][len(coins)] = None
            else:
                dp[N][len(coins)] = min(dp[N][len(coins)], value)
        else:
            if dp[N][len(coins)] == 0 or dp[N][len(coins)] is None:
                dp[N][len(coins)] = value
            else:
                dp[N][len(coins)] = min(dp[N][len(coins)], value)
    return dp[N][len(coins)]

Work: O(N*K).
Span: O(k)

