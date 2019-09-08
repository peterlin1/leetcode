# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        Write a program to find the node at which the intersection of two singly linked lists begins.

        Runtime: 212 ms, faster than 13.87% of Python online submissions for Intersection of Two Linked Lists.
        Memory Usage: 41.6 MB, less than 100.00% of Python online submissions for Intersection of Two Linked Lists.


        Parameters
        ----------
        headA : ListNode
        headB : ListNode


        Returns
        -------
        ret : ListNode

        """
        l_1 = headA
        l_2 = headB
        l_1_c = l_2_c = 0
        while l_1:
            l_1 = l_1.next
            l_1_c += 1

        while l_2:
            l_2 = l_2.next
            l_2_c += 1

        if l_1 is not l_2:
            return

        _traverse = 0
        if l_1_c >= l_2_c:
            _traverse = l_1_c - l_2_c
            # Longer list will be denoted by l_1
            l_1 = headA
            l_2 = headB
        else:
            _traverse = l_2_c - l_1_c
            # Longer list will be denoted by l_1
            l_1 = headB
            l_2 = headA

        while _traverse > 0:
            l_1 = l_1.next
            _traverse -= 1

        while l_1 is not l_2:
            l_1 = l_1.next
            l_2 = l_2.next

        return l_1


if __name__ == "__main__":
    a = ListNode(4)
    b = ListNode(1)
    c = ListNode(8)
    d = ListNode(4)
    e = ListNode(5)

    f = ListNode(5)
    g = ListNode(0)
    h = ListNode(1)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    f.next = g
    g.next = h
    h.next = c
    print(Solution().getIntersectionNode(a, f).val)
