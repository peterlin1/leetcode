# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def minDepth(self, root):
        """
        Given a binary tree, find its minimum depth.

        The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf
        node.

        Note: A leaf is a node with no children.

        Example:

        Given binary tree [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
        return its minimum depth = 2.

        Runtime: 56 ms, faster than 38.38% of Python3 online submissions for Minimum Depth of Binary Tree.
        Memory Usage: 16.1 MB, less than 8.11% of Python3 online submissions for Minimum Depth of Binary Tree.


        Parameters
        ----------
        root : TreeNode


        Returns
        -------
        ret : int

        """
        if root:
            if not root.left and not root.right:
                return 1
            elif root.left and root.right:
                return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
            elif root.left:
                return self.minDepth(root.left) + 1
            else:
                return self.minDepth(root.right) + 1
        else:
            return 0


if __name__ == "__main__":
    ex = TreeNode(3)
    ex.left = TreeNode(9)
    ex.right = TreeNode(20)

    ex.right.left = TreeNode(15)
    ex.right.right = TreeNode(7)

    print(Solution().minDepth(ex))
