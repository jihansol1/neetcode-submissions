
# DLL's node class including key:val pair + prev, next ptr for each node
class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # initialize a map
        self.cache = {}
        # initialize capacity 
        self.capacity = capacity

        # initialize head, tail pointers, and connect them
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    # helper function -> remove node from linked list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # helper function -> insert node to tail position
    def insert(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node



    # return the value corresponding to the key if the key exists, otherwise return -1
    def get(self, key: int) -> int:
        if key in self.cache:
            # remove node from DLL
            self.remove(self.cache[key])
            # insert node to DLL tail
            self.insert(self.cache[key])

            return self.cache[key].val
        return -1

    # update the val of key if key exists, otherwise add key-val pair to cache. If capacity exceeded, delete LRU item
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove node from DLL
            self.remove(self.cache[key])
        # create new updated node 
        self.cache[key] = Node(key, value)
        # insert new node to DLL tail
        self.insert(self.cache[key])

        # if capacity exceeded -> remove LRU item
        if len(self.cache) > self.capacity:
            # lru is first item in DLL
            lru = self.head.next
            # remove lru from DLL
            self.remove(lru)
            # remove lru from map
            del self.cache[lru.key]
        
