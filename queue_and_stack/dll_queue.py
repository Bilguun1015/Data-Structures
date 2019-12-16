import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

#FIFO
class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()
    #back of the queue
    def enqueue(self, value):
       self.storage.add_to_tail(value)
       self.size += 1
    #remove and return front of the queue
    def dequeue(self):
        if self.size is not 0:
            value = self.storage.remove_from_head()
            self.size -= 1
            return value
        else:
            return None   
    #returns number of items in the queue
    def len(self):
        return self.size
