# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def recursive_compare(node,low,up):
            if not node:
                return True
            if(node.val <= low or node.val >= up):
                return False
            if not recursive_compare(node.right,node.val,up):
                return False
            if not recursive_compare(node.left,low,node.val):
                return False
            return True
        """
        :type root: TreeNode
        :rtype: bool
        """
        return recursive_compare(root,float('-inf'),float('inf'))