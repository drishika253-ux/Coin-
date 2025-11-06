class Solution(object):
    def coinChange(self, coins, amount):
        # Edge cases
        if not coins:
            return -1
        if amount == 0:
            return 0

        # Initialize DP array
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # base case

        # Build up the DP array
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # Return -1 if no valid combination found
        return dp[amount] if dp[amount] != amount + 1 else -1




        
