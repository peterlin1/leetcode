class Node:
    def __init__(self, end=None, prev=None, key=None, val=None):
        self.end = end
        self.prev = prev
        self.key = key
        self.val = val


class LRUCache(object):
    """
    Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following
    operations: get and put.

    get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
    put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it
    should invalidate the least recently used item before inserting a new item.

    The cache is initialized with a positive capacity.

    Follow up:
    Could you do both operations in O(1) time complexity?

    18 / 18 test cases passed.
    Status: Accepted
    Runtime: 232 ms
    Memory Usage: 23.7 MB

    """

    def __init__(self, capacity):
        """

        Parameters
        ----------
        capacity : int

        """

        self.capacity = capacity
        self.q_map = {}
        self.q_first = None
        self.q_last = None
        self.q_length = 0

    def get(self, key):
        """
        Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.


        Parameters
        ----------
        key : int


        Returns
        -------
        ret : int

        """

        if key in self.q_map:
            if self.q_map[key] is self.q_first:
                return self.q_map[key].val

            if self.q_map[key].end is not None:
                self.q_map[key].end.prev = self.q_map[key].prev
            if self.q_map[key].prev is not None:
                self.q_map[key].prev.end = self.q_map[key].end

            if self.q_map[key] is not self.q_first:
                if self.q_map[key] is self.q_last:
                    self.q_last = self.q_map[key].prev
                self.q_map[key].end = self.q_first
                self.q_first.prev = self.q_map[key]
                self.q_first = self.q_map[key]
            self.q_map[key].prev = None

            return self.q_map[key].val
        return -1

    def put(self, key, value):
        """
        Set or insert the value if the key is not already present. When the cache reached its capacity, it should
        invalidate the least recently used item before inserting a new item.


        Parameters
        ----------
        key : int

        value : int

        """

        if self.q_first:
            if key in self.q_map:
                c_node = self.q_map[key]
                c_node.val = value
                if c_node is self.q_first:
                    return

                if c_node.end is not None:
                    c_node.end.prev = c_node.prev
                if c_node.prev is not None:
                    c_node.prev.end = c_node.end

                if c_node is not self.q_first:
                    if c_node is self.q_last:
                        self.q_last = c_node.prev
                    c_node.end = self.q_first
                    self.q_first.prev = c_node
                    self.q_first = c_node
                c_node.prev = None
            else:
                n_node = Node(key=key, val=value)
                n_node.end = self.q_first

                self.q_length += 1
                if self.q_length > self.capacity:
                    del self.q_map[self.q_last.key]
                    self.q_last = self.q_last.prev
                    self.q_length -= 1

                self.q_map[key] = n_node
                self.q_first.prev = n_node
                self.q_first = n_node

        else:
            self.q_first = self.q_last = self.q_map[key] = Node(key=key, val=value)
            self.q_length += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)

    # returns 1
    cache.get(1)
    # evicts key 2
    cache.put(3, 3)
    # returns - 1(not found)
    cache.get(2)
    # evicts key 1
    cache.put(4, 4)
    # returns - 1(not found)
    cache.get(1)
    # returns 3
    cache.get(3)
    # returns 4
    cache.get(4)

    # cache.put(2, 1)
    # cache.put(3, 2)
    # cache.get(3)
    # cache.get(2)
    # cache.put(4, 3)
    # cache.get(2)
    # cache.get(3)
    # cache.get(4)

    d_cache = cache.q_first
    while d_cache:
        print(d_cache.val)
        d_cache = d_cache.end
