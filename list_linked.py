# File: list_linked.py
# Date: April 13, 2021
# Author: COMP 120 class
# Description: Linked list implementation of List ADT.

class Node:
    def __init__(self, item, next = None):
        """ Constructor.  Creates a node."""
        self.next = next
        self.item = item

class LinkedList:
    def __init__(self):
        """ Constructor.  Creates an empty list."""
        self.front = None
        self.back = None
        self.len = 0

    def append(self, x):
        """ Append x to the end of the list """
        if self.len == 0:
            self.front = self.back = Node(x)
        else:
            self.back.next = Node(x)
            self.back = self.back.next
        self.len += 1

    def __len__(self):
        """ Returns length of list """
        return self.len

    def __str__(self):
        """ Returns string representation of list """
        if self.front == None:
            return "[]"
        else:
            s = "["
            cur = self.front
            while cur.next != None:
                s += str(cur.item) + ", "
                cur = cur.next
            s += str(cur.item) + "]"
        return s

    def __getitem__(self, i):
        """ 
        Returns item at index i of list.
        Raises IndexError if i is not valid
        """

        # Handle negative index
        if i < 0:
            i += self.len

        # Check for invalid index
        if i < 0 or i >= self.len:
            raise IndexError

        cur = self.front
        index = 0
        while index < i:
            cur = cur.next
            index += 1

        return cur.item

    def insert(self, i, x):
        """
        Insert item x into the list at index i.
        """
        
        # Python list class actually allows
        # any integer, but to keep things simple,
        # we'll require i to be 0 <= i <= self.len
        if i > self.len or i < 0:
            raise IndexError

        if i == 0:
            self.front = Node(x, self.front)
            if self.len == 0:
                self.back = self.front
            self.len += 1
        elif i == self.len:
            self.append(x)
        else:
            current = self.front
            y = 0
            while y < i - 1:
                y += 1
                current = current.next
            current.next = Node(x, current.next)
            self.len += 1

    def pop(self, i = 0):
        """
        Remove and return the item in the list
        at index i.  i defaults to 0.
        IndexError is raised if invalid index.
        """

        # Handle negative index
        if i < 0:
            i += self.len
        
        # Check for out of range index
        if i < 0 or i >= self.len:
            raise IndexError

        if i == 0:
            item = self.front.item
            self.front = self.front.next
            if self.len == 1:
                self.back = None
        else:
            current = self.front
            y = 0
            while y < i - 1:
                y += 1
                current = current.next
            item = current.next.item
            current.next = current.next.next
            if i == self.len - 1:
                self.back = current

        self.len -= 1
        return item