# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def middleNode(self, head):
        """
        Given a non-empty, singly linked list with head node head, return a middle node of linked list.

        If there are two middle nodes, return the second middle node.

        Note:
        The number of nodes in the given list will be between 1 and 100.

        Runtime: 32 ms, faster than 36.20% of Python3 online submissions for Middle of the Linked List.
        Memory Usage: 13.9 MB, less than 7.14% of Python3 online submissions for Middle of the Linked List.


        Parameters
        ----------
        head : ListNode


        Returns
        -------
        ret : ListNode

        """

        pointer = head.next
        ln = 1
        while pointer:
            ln += 1
            pointer = pointer.next

        ln = ln // 2 + 1

        pointer = head
        while ln != 1:
            pointer = pointer.next
            ln -= 1

        return pointer


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    print(Solution().middleNode(a).val)
