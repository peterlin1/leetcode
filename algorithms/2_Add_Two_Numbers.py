# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.

        Runtime: 96 ms, faster than 11.51% of Python3 online submissions for Add Two Numbers.
        Memory Usage: 13.3 MB, less than 24.51% of Python3 online submissions for Add Two Numbers.


        Parameters
        ----------
        l1 : ListNode
        l2 : ListNode


        Returns
        -------
        ret : ListNode

        """

        ret = ListNode(0)
        ret_pointer = ListNode(None)
        temp_node = ret

        def add(la, lb, exp):
            sum_node = la.val + lb.val + exp
            return sum_node % 10, ListNode(sum_node // 10)

        while l1 or l2:
            ret_pointer.next = temp_node
            ret_pointer = ret_pointer.next
            if l1 and l2:
                ret_pointer.val, temp_node = add(l1, l2, ret_pointer.val)
                l1 = l1.next
                l2 = l2.next
            elif l1:
                ret_pointer.val, temp_node = add(l1, ListNode(0), ret_pointer.val)
                l1 = l1.next
            else:
                ret_pointer.val, temp_node = add(ListNode(0), l2, ret_pointer.val)
                l2 = l2.next

        if temp_node.val is 1:
            ret_pointer.next = temp_node
        # Output is in reversed order
        return ret


def int_to_listnode(num):
    ret = ListNode(None)
    ret_pointer = ret
    num_str = str(num)[::-1]

    for digit in num_str:
        ret_pointer.next = ListNode(int(digit))
        ret_pointer = ret_pointer.next
    return ret.next


def print_listnode(ln):
    ret = []
    while ln:
        ret.append(ln.val)
        ln = ln.next
    print(ret)


if __name__ == "__main__":
    # [7, 0, 8]
    Solution().addTwoNumbers(int_to_listnode(342), int_to_listnode(465))

