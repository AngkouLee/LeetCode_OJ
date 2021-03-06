#Given an array of integers, every element appears twice except for one. Find that single one.
#Note:
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
    	#Using bit operator, knowledge short for 'Bit Manipulation'
    	result = 0
    	for num in nums:
    		result = result^num

    	return result
