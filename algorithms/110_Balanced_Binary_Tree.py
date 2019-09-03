# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        Given a binary tree, determine if it is height-balanced.

        For this problem, a height-balanced binary tree is defined as:

        a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

        Example 1:

        Given the following tree [3,9,20,null,null,15,7]:

            3
           / \
          9  20
            /  \
           15   7

        Return true.

        Example 2:

        Given the following tree [1,2,2,3,3,null,null,4,4]:

               1
              / \
             2   2
            / \
           3   3
          / \
         4   4
        Return false.

        Runtime: 72 ms, faster than 35.98% of Python3 online submissions for Balanced Binary Tree.
        Memory Usage: 19.5 MB, less than 5.72% of Python3 online submissions for Balanced Binary Tree.


        Parameters
        ----------
        root : TreeNode


        Returns
        -------
        ret : bool

        """

        # 104: Maximum Depth of Binary Tree
        def _maxDepth(node):
            if node:
                if not node.left and not node.right:
                    return 1
                elif node.left and node.right:
                    return max(_maxDepth(node.left), _maxDepth(node.right)) + 1
                elif node.left:
                    return _maxDepth(node.left) + 1
                else:
                    return _maxDepth(node.right) + 1
            else:
                return 0

        if not root:
            return True

        if (abs(_maxDepth(root.left) - _maxDepth(root.right)) <= 1) and (self.isBalanced(root.left)) and \
                (self.isBalanced(root.right)):
            return True

        return False


if __name__ == "__main__":
    ex = TreeNode(3)
    ex.left = TreeNode(9)
    ex.right = TreeNode(20)

    ex.right.left = TreeNode(15)
    ex.right.right = TreeNode(7)

    print(Solution().isBalanced(ex))