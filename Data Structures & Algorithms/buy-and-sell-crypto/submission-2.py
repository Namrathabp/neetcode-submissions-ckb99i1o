class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_pro:
                max_pro = price - min_price
        # l = 0
        # r = len(prices)-1
        # max_nb = max(prices)
        # print(max_nb)
        # print(prices[r])
        # while l < r:
        #     pro = prices[r] - prices[l]
        #     print(pro)
        #     print(max_pro)
        #     if pro > max_pro and prices[r] != max_nb:
        #         max_pro = pro
        #         r -= 1
        #     elif pro == max_pro and prices[r] != max_nb:
        #         r -= 1
        #     else:
        #         l += 1
        return max_pro                
        