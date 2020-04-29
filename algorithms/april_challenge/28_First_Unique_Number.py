from collections import Counter, deque


class FirstUnique(object):
    """
    You have a queue of integers, you need to retrieve the first unique integer in the queue.

    Implement the FirstUnique class:
    FirstUnique(int[] nums) Initializes the object with the numbers in the queue.

    int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such
    integer.

    void add(int value) insert value to the queue.

    Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^8
    1 <= value <= 10^8
    At most 50000 calls will be made to showFirstUnique and add.

    17 / 17 test cases passed.
    Status: Accepted
    Runtime: 808 ms
    Memory Usage: 55.6 MB

    """

    def __init__(self, nums):
        """

        Parameters
        ----------
        nums : list

        """

        self._mem = deque()
        self._m_map = Counter(nums)
        for val in nums:
            if self._m_map[val] == 1:
                self._mem.append(val)

    def showFirstUnique(self):
        """
        Returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.

        """

        try:
            return self._mem[0]
        except IndexError:
            return -1

    def add(self, value):
        """
        Insert value to the queue.


        Parameters
        ----------
        value

        """

        self._m_map[value] += 1
        if self._m_map[value] == 1:
            self._mem.append(value)
        else:
            while self._mem and (self._m_map[self._mem[0]] > 1):
                self._mem.popleft()

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)


if __name__ == "__main__":
    ex1 = FirstUnique([2, 3, 5])
    print(ex1.showFirstUnique())
    ex1.add(5)
    print(ex1.showFirstUnique())
    ex1.add(2)
    print(ex1.showFirstUnique())
    ex1.add(3)
    print(ex1.showFirstUnique())
