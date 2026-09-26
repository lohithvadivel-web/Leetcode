# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """

        if root is None:
            return []

        result = []

        def dfs(node, path):
            if node.left is None and node.right is None:
                result.append(path + str(node.val))
                return

            path += str(node.val) + "->"

            if node.left:
                dfs(node.left, path)

            if node.right:
                dfs(node.right, path)

        dfs(root, "")

        return result
