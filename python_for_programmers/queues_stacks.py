from node import Node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print("adding " + str(item_to_add.get_value()) + " to the queue")
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("no more room")

    def dequeue(self):
        if self.get_size() > 0:
            item_to_remove = self.head
            print(str(item_to_remove.get_value()) + " is served")
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("queue is empty")
        
    def peek(self):
        if self.size > 0:
            return self.head.get_value()
        else:
            print("no orders waiting")
    
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("out of space")
    
    def pop(self):
        if self.size > 0:
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("stack is empty")

    def peek(self):
        if self.size > 0:
            return self.top_item.get_value()
        else:
            print("nothing to see here")

    def is_empty(self):
        return self.size == 0