from doubly_linked_list import DoublyLinkedList
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.cache = DoublyLinkedList()
        self.storage = {}
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if self.storage.get(key, False):
            d_value_node = self.cache.get_node_from_key(key)
            self.cache.move_to_front(d_value_node)
        return self.storage.get(key, None)

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        d_value = [key, value]
        if not self.storage.get(key, False):
            if len(self.storage) == self.limit:
                del self.storage[self.cache.tail.value[0]]
                self.cache.delete(self.cache.tail)
            self.cache.add_to_head(d_value)
            self.storage[key] = value
        else:
            d_value_node = self.cache.get_node_from_key(key)
            d_value_node.value = d_value
            self.cache.move_to_front(d_value_node)
            self.storage[key] = value