import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

#FIFO
class Queue:
    def __init__(self):
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()
    #back of the queue
    def enqueue(self, value):
       self.storage.add_to_tail(value)
    #remove and return front of the queue
    def dequeue(self):
        if self.storage.length is not 0:
            value = self.storage.remove_from_head()
            return value
        else:
            return None   
    #returns number of items in the queue
    def len(self):
        return self.storage.length
