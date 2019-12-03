# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def sumOfLeftLeaves(self, root):
        """
        Find the sum of all left leaves in a given binary tree.

        Example:

            3
           / \
          9  20
            /  \
           15   7

        There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

        Runtime: 24 ms, faster than 98.95% of Python3 online submissions for Sum of Left Leaves.
        Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Sum of Left Leaves.


        Parameters
        ----------
        root


        Returns
        -------
        ret : int

        """

        ret = 0
        if root:
            n_queue = [(root, 0)]
        else:
            return ret

        while len(n_queue) > 0:
            t_root = n_queue.pop(0)

            if t_root[0].left is None and t_root[0].right is None and t_root[1] is 1:
                ret += t_root[0].val
                continue
            if t_root[0].right is not None:
                n_queue.append((t_root[0].right, 0))
            if t_root[0].left is not None:
                n_queue.append((t_root[0].left, 1))

        return ret


if __name__ == "__main__":
    ex1 = TreeNode(3)
    a = TreeNode(9)
    b = TreeNode(20)
    c = TreeNode(15)
    d = TreeNode(7)
    ex1.left = a
    ex1.right = b
    b.left = c
    b.right = d

    print(Solution().sumOfLeftLeaves(ex1))
