def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    #easy Greedy apply
    for i in range(1, len(prices)):
        t = prices[i] - prices[i - 1]
        if t > 0:
            profit += t
    return profit