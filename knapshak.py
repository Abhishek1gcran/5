def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a 2D array to store the maximum values for each subproblem
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            # If the current item can fit in the remaining capacity
            if weights[i - 1] <= j:
                # Take the maximum value between including and excluding the current item
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                # Exclude the current item as it cannot fit
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][capacity]


# Example usage:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8
max_value = knapsack(weights, values, capacity)
print("Maximum value:", max_value)
