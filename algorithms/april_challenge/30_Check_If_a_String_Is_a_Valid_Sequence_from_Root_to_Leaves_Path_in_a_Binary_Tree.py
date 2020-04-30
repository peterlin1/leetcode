# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def isValidSequence(self, root, arr):
        """
        Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given
        string is a valid sequence in such binary tree.

        We get the given string from the concatenation of an array of integers arr and the concatenation of all values
        of the nodes along a path results in a sequence in the given binary tree.

        1 <= arr.length <= 5000
        0 <= arr[i] <= 9
        Each node's value is between [0 - 9].

        63 / 63 test cases passed.
        Status: Accepted
        Runtime: 112 ms
        Memory Usage: 15.4 MB


        Parameters
        ----------
        root : TreeNode

        arr : list


        Returns
        -------
        ret : bool

        """

        def _find_key(node, idx):
            if not node or idx == len(arr):
                return False

            if arr[idx] == node.val:
                if not node.left and not node.right and idx == len(arr) - 1:
                    return True

                _l_ret = _find_key(node.left, idx + 1)
                _r_ret = _find_key(node.right, idx + 1)
                return _l_ret or _r_ret
            return False

        return _find_key(root, 0)


if __name__ == "__main__":
    ex1 = TreeNode(0)
    a = TreeNode(1)
    b = TreeNode(0)
    c = TreeNode(0)
    d = TreeNode(1)
    e = TreeNode(0)
    f = TreeNode(1)
    g = TreeNode(0)
    h = TreeNode(0)

    ex1.left = a
    ex1.right = b
    a.left = c
    a.right = d
    b.left = e
    c.right = f
    d.left = g
    d.right = h

    print(Solution().isValidSequence(ex1, [0, 0, 0]))

