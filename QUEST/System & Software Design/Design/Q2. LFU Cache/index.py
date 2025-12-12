class Node:
    def __init__(self, key, value, freq):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        # Insert node right before tail (most recent)
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def pop_left(self):
        # Pop least recently used (head.next)
        if self.head.next == self.tail:
            return None
        lru = self.head.next
        self.remove(lru)
        return lru

    def is_empty(self):
        return self.head.next == self.tail


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        self.key_table = {}  # key -> node
        self.freq_table = {}  # freq -> DLL
        self.min_freq = 0

    def update_freq(self, node):
        freq = node.freq
        self.freq_table[freq].remove(node)

        # If this was the only node of this freq and freq == min_freq, increase min_freq
        if self.freq_table[freq].is_empty():
            if freq == self.min_freq:
                self.min_freq += 1

        # Increase the node's frequency
        node.freq += 1
        new_freq = node.freq

        if new_freq not in self.freq_table:
            self.freq_table[new_freq] = DoublyLinkedList()

        self.freq_table[new_freq].insert(node)

    def get(self, key: int) -> int:
        if key not in self.key_table or self.capacity == 0:
            return -1

        node = self.key_table[key]
        self.update_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_table:
            # Update existing
            node = self.key_table[key]
            node.value = value
            self.update_freq(node)
            return

        # Evict if needed
        if self.size == self.capacity:
            # Remove LFU + LRU key
            dll = self.freq_table[self.min_freq]
            lru_node = dll.pop_left()
            del self.key_table[lru_node.key]
            self.size -= 1

        # Insert new key with freq = 1
        new_node = Node(key, value, 1)
        self.key_table[key] = new_node

        if 1 not in self.freq_table:
            self.freq_table[1] = DoublyLinkedList()

        self.freq_table[1].insert(new_node)

        self.min_freq = 1
        self.size += 1
