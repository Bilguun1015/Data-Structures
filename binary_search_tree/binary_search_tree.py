import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.storage_queue = Queue()
        self.storage_stack = Stack()

    # Insert the given value into the tree
    def insert(self, value):
        #If inserting we must already have a tree/root
        #if value is less than self.value self.left, make a new tree/node if empty otherwise
        #keep going (recursion)
        # if greater than or equal to go right, make a new tree/node if empty otherwise 
        #keep going (recursion)
        if self.value:
            if value < self.value:
                if self.left:
                    return self.left.insert(value)
                else:
                    self.left = BinarySearchTree(value)
                    return self.left.value
            elif value >= self.value:
                if self.right:
                    return self.right.insert(value)
                else:
                    self.right = BinarySearchTree(value)
                    return self.right.value
        else:
            self.value = value
            return self.value


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target  == self.value, return it
        #otherwise go left or right based on smaller or bigger
        if target == self.value:
            return True
        elif target >= self.value:
            if self.right:
                if self.right.value == target:
                    return True
                else:
                    return self.right.contains(target)
            else:
                return False
        elif target < self.value:
            if self.left:
                if self.left.value == target:
                    return True
                else:
                    return self.left.contains(target)
            else:
                return False
    # Return the maximum value found in the tree
    def get_max(self):
        # if right exist go right
        # otherwise return self.value
        if self.right:
            return self.right.get_max()
        else:
            return self.value
    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)

        if self.left:
            self.left.for_each(cb)

     # DAY 2 Project -----------------------
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.len() > 0:
            current_node = queue.dequeue()
            print(current_node.value)
            if current_node.right:
                queue.enqueue(current_node.right)
            if current_node.left:
                queue.enqueue(current_node.left)
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.right:
                stack.push(current_node.right)
            if current_node.left:
                stack.push(current_node.left)
    # STRETCH Goals -------------------------
    # Note: Research may be required
    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass
    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
