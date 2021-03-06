#Given an array of integers, find if the array contains any duplicates. 
#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
    	dictionary = {}
    	for num in nums:
    		if num in dictionary:
    			return True
    		else:
    			dictionary.update({num:None})
    	return False