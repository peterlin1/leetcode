# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def hasCycle(self, head):
        """
        Given a linked list, determine if it has a cycle in it.

        To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed)
        in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

        Example 1:
        Input: head = [3,2,0,-4], pos = 1
        Output: true
        Explanation: There is a cycle in the linked list, where tail connects to the second node.

        Implementation of Floyd's Tortoise and Hare algorithm
        Runtime: 32 ms, faster than 93.65% of Python online submissions for Linked List Cycle.
        Memory Usage: 18.1 MB, less than 85.11% of Python online submissions for Linked List Cycle.

        Parameters
        ----------
        head : ListNode

        Returns
        -------
        ret : bool

        """
        if not head or not head.next:
            return False
        tortoise = hare = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

            if hare == tortoise:
                return True
        return False


if __name__ == "__main__":
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(4)

    a.next = b
    b.next = c
    c.next = d
    d.next = b

    print(Solution().hasCycle(a))

