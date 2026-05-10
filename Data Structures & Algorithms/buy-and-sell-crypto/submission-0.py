class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lastMin = prices[0]

        for p in prices[1:]:
            if p > lastMin:
                diff = p - lastMin
                res = max(res, diff)
            lastMin = min(lastMin, p)
        
        return res