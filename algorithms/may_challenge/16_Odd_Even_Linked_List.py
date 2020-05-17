# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def oddEvenList(self, head):
        """
        Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are
        talking about the node number and not the value in the nodes.

        You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

        Note:
        The relative order inside both the even and odd groups should remain as it was in the input.
        The first node is considered odd, the second node even and so on ...

        71 / 71 test cases passed.
        Status: Accepted
        Runtime: 84 ms
        Memory Usage: 15.8 MB


        Parameters
        ----------
        head : ListNode


        Returns
        -------
        ret : ListNode

        """

        ret = l1 = ListNode()
        _l2 = l2 = ListNode()

        while head:
            l1.next = head
            l2.next = head.next
            l1 = l1.next
            l2 = l2.next
            try:
                head = head.next.next
            except AttributeError:
                head = None

        l1.next = _l2.next
        return ret.next


if __name__ == "__main__":
    d = ListNode(val=5)
    c = ListNode(val=4, next=d)
    b = ListNode(val=3, next=c)
    a = ListNode(val=2, next=b)
    ex1 = ListNode(val=1, next=a)

    Solution().oddEvenList(ex1)
