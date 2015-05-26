#Say you have an array for which the ith element is the price of a given stock on day i.

#Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 
#However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

class Solution:
	# @param {integer[]} prices
	# @return {integer}
	def maxProfit(self, prices):
		if len(prices) < 2:
			return 0
		
		profit = 0
		lowPrice = prices[0]
		highPrice = prices[0]
		for idx, price in enumerate(prices):
			if idx+1 >= len(prices):
				break
			nextPrice = prices[idx+1]
			if price > nextPrice:
				lowPrice = nextPrice
				highPrice = nextPrice
			else:
				lowPrice = price
				highPrice = nextPrice
				profit = profit + (highPrice - lowPrice)

		return profit

