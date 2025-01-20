"""
Stack implementation by Caleb Zierenberg
Created 1/20/2025



Stack class using linked nodes
methods:
push() - add a value to the top of the stack
pop() - return and remove value at top of stack
peek() - return top value without removing
is_empty() - returns true if empty, false otherwise
size() - returns number of values in stack
clear() - removes all values from stack
contains() - returns true if stack contains specified value, false otherwise
to_list() - returns a list of all values in stack

Stack will also be iterable

"""

 


class Stack():
    class Node():
        def __init__(self, value):
            self.value = value
            self.next = None

    class _Iterator():
        def __init__(self, start_node):
            self.current = start_node

        def __iter__(self):
            return self

        def __next__(self):
            if self.current == None:
                raise StopIteration
            else:
                value = self.current.value
                self.current = self.current.next
                return value


    def __iter__(self):
        return self._Iterator(self.top)        


    def __init__(self):
        self.top = None
        self._size = 0


    def push(self, value):
        node = self.Node(value)
        current = self.top

        self.top = node
        node.next = current
        self._size += 1
        

    def pop(self):
        current = self.top

        if self._size > 0:
            self._size -= 1
            self.top = current.next
            return current.value
        else:
            return None

    def peek(self):
        if self._size > 0:
            return self.top.value
        else:
            return None

    def is_empty(self):
        return (self._size<1)

    def size(self):
        return self._size

    def clear(self):
        self.top = None
        self._size = 0

    def contains(self, value):
        current = self.top
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_list(self):
        current = self.top
        lyst = []
        while current != None:
            lyst.append(current.value)
            current = current.next
        return lyst











