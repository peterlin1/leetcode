import random


class RandomizedSet(object):
    """
    Design a data structure that supports all following operations in average O(1) time.

    insert(val): Inserts an item val to the set if not already present.
    remove(val): Removes an item val from the set if present.
    getRandom: Returns a random element from current set of elements. Each element must have the same probability of
    being returned.

    Runtime: 100 ms, faster than 83.93% of Python3 online submissions for Insert Delete GetRandom O(1).
    Memory Usage: 17.9 MB, less than 42.04% of Python3 online submissions for Insert Delete GetRandom O(1).

    """

    def __init__(self):
        """
        Initialize your data structure here.

        """

        self.mem = {}
        self.ds = []
        self.rng = random.Random()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.


        Parameters
        ----------
        val : int


        Returns
        -------
        ret : bool

        """

        if val in self.mem:
            return False

        self.ds.append(val)
        self.mem[val] = len(self.ds) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.


        Parameters
        ----------
        val : int


        Returns
        -------
        ret : bool

        """

        try:
            idx = self.mem[val]
            last_val = self.ds[-1]
            self.ds[idx] = last_val
            self.mem[last_val] = idx
            del self.mem[val]
            self.ds.pop()

            return True
        except KeyError:
            return False

    def getRandom(self):
        """
        Get a random element from the set.


        Returns
        -------
        ret : int

        """

        return self.ds[self.rng.randint(0, len(self.ds))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
if __name__ == "__main__":
    ex1 = RandomizedSet()
    ex1.insert(1)
    ex1.remove(2)
    ex1.insert(2)
    ex1.getRandom()
    ex1.remove(1)
    ex1.insert(2)
    ex1.getRandom()
