class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		if not matrix:
			return []
		left, right, top, down, res = 0, len(matrix[0])-1, 0, len(matrix)-1, []
		while left <= right and top <= down:
			res.extend(matrix[top][left:right+1]) # left to right
			top += 1 
			for i in xrange(top, down+1): # top to down
				res.append(matrix[i][right])
			right -= 1
			if top <= down:
				res.extend(matrix[down][left:right+1][::-1]) # right to left
				down -= 1
			if left <= right:
				for i in xrange(down, top-1, -1): # bottom to up
					res.append(matrix[i][left])
				left += 1
		return res