# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def bstFromPreorder(self, preorder):
        """
        Return the root node of a binary search tree that matches the given preorder traversal.

        (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a
        value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder
        traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

        Note:
        1 <= preorder.length <= 100
        The values of preorder are distinct.

        110 / 110 test cases passed.
        Status: Accepted
        Runtime: 36 ms
        Memory Usage: 13.7 MB


        Parameters
        ----------
        preorder : list


        Returns
        -------
        ret : TreeNode

        """

        ret = TreeNode(preorder[0])
        queue = [ret]

        for idx in range(1, len(preorder)):
            pointer = queue[-1]
            if preorder[idx] < pointer.val:
                n_p = TreeNode(preorder[idx])
                pointer.left = n_p
                queue.append(n_p)
            else:
                while queue and preorder[idx] > queue[-1].val:
                    pointer = queue.pop()
                pointer.right = TreeNode(preorder[idx])
                queue.append(pointer.right)

        return ret
