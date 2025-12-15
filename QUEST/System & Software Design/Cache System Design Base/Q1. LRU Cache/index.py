class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> node

        # Dummy head and tail (for easier insert/remove)
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Helper: remove node from the linked list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # Helper: insert node at right before tail (most recently used)
    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # Move to most recently used
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing node
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            # Create new node
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)

            # If over capacity, evict least recently used (head.next)
            if len(self.cache) > self.cap:
                lru = self.head.next
                self.remove(lru)
                del self.cache[lru.key]
