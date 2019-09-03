# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def hasPathSum(self, root, sum):
        """
        Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values
        along the path equals the given sum.

        Note: A leaf is a node with no children.

        Example:

        Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
        return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22

        Depth-first search.

        Runtime: 48 ms, faster than 86.22% of Python3 online submissions for Path Sum.
        Memory Usage: 15.6 MB, less than 5.45% of Python3 online submissions for Path Sum.


        Parameters
        ----------
        root : TreeNode

        sum : int


        Returns
        -------
        ret : bool

        """
        if not root:
            return False

        if not root.left and not root.right:
            if (sum - root.val) is not 0:
                return False
            return True
        elif root.left and root.right:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        elif root.left:
            return self.hasPathSum(root.left, sum - root.val)
        else:
            return self.hasPathSum(root.right, sum - root.val)


if __name__ == "__main__":
    ex = TreeNode(5)
    ex.left = TreeNode(4)
    ex.right = TreeNode(8)

    ex.left.left = TreeNode(11)
    ex.left.left.left = TreeNode(7)
    ex.left.left.right = TreeNode(2)

    ex.right.left = TreeNode(13)
    ex.right.right = TreeNode(4)
    ex.right.right.right = TreeNode(1)

    print(Solution().hasPathSum(ex, 22))
