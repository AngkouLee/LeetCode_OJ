# Given a binary tree, return the preorder traversal of its nodes' values.
# For example:
# Given binary tree {1,#,2,3},return [1,2,3].

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
    	result = []
    	self.inTra(root,result)

    	return result

    def inTra(self, node, intArray):
    	if not node:
    		return None
    	self.inTra(node.left, intArray)
        val = node.val
        intArray.append(val)
    	self.inTra(node.right, intArray)