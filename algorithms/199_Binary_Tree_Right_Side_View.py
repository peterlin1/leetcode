# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can
        see ordered from top to bottom.

        Runtime: 36 ms, faster than 84.75% of Python3 online submissions for Binary Tree Right Side View.
        Memory Usage: 13.8 MB, less than 5.26% of Python3 online submissions for Binary Tree Right Side View.


        Parameters
        ----------
        root : TreeNode


        Returns
        -------
        ret : list

        """

        ret = []
        if root:
            n_queue = [(root, 0)]
        else:
            return ret

        while len(n_queue) > 0:
            t_root = n_queue.pop(0)
            try:
                ret[t_root[1]] = t_root[0].val
            except IndexError:
                ret.append(t_root[0].val)

            if t_root[0].left is not None:
                n_queue.append((t_root[0].left, t_root[1] + 1))
            if t_root[0].right is not None:
                n_queue.append((t_root[0].right, t_root[1] + 1))

        return ret


if __name__ == "__main__":
    ex = TreeNode(1)
    ex.left = TreeNode(2)
    ex.right = TreeNode(3)

    ex.left.left = TreeNode(5)

    ex.right.left = TreeNode(5)
    ex.right.right = TreeNode(6)

    print(Solution().rightSideView(ex))
