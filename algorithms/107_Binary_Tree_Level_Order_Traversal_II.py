# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def levelOrderBottom(self, root):
        """
        Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right,
        level by level from leaf to root).

        For example:
        Given binary tree [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7

        return its bottom-up level order traversal as:
        [
          [15,7],
          [9,20],
          [3]
        ]

        Runtime: 40 ms, faster than 82.20% of Python3 online submissions for Binary Tree Level Order Traversal II.
        Memory Usage: 14.8 MB, less than 7.41% of Python3 online submissions for Binary Tree Level Order Traversal II.


        Parameters
        ----------
        root : TreeNode


        Returns
        -------
        ret : list

        """
        ret = []

        def _add_hierchial(level, *args):
            for node in args:
                if node:
                    try:
                        ret[level].extend([node.val])
                    except IndexError:
                        ret.insert(level, [node.val])
                    _add_hierchial(level - 1, node.left, node.right)

        _add_hierchial(-1, root)
        return ret


if __name__ == "__main__":
    ex = TreeNode(3)
    ex.left = TreeNode(9)
    ex.right = TreeNode(20)

    ex.right.left = TreeNode(15)
    ex.right.right = TreeNode(7)

    print(Solution().levelOrderBottom(ex))
