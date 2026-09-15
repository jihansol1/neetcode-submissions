
class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    # need a hashmap to store key:address in linked list pairs
    # need a doubly linked list to store pairs used in order to access LRU pair -> will be head
    # whenever a pair is accessed, move it to tail


    def __init__(self, capacity: int):
        # initialize the LRU cache of size capacity
        self.cache = {}
        self.capacity = capacity

        # initialize the head and tail pointers and connect them
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head 

    # removing the node from its location
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        

    # attaching the node to the tail
    def insert(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node



    def get(self, key: int) -> int:
        # return the value corresponding to the key if the key exists, otherwise -1

        # if key in map -> get key:val in linked list and update to the tail
        if key in self.cache: 
            # remove node from its position
            self.remove(self.cache[key])
            # add node to tail
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
            

    def put(self, key: int, value: int) -> None:
        # update val of key if the key exists. otherwise, add the key-val pair to the cache
        # if adding new pair exceeds capacity, remove the least recently used key

        # if key exists -> update 
        if key in self.cache:
            # remove from DLL
            self.remove(self.cache[key])
        # add key:val node to map
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key]) 

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]





