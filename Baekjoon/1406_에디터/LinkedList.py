# 미완

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:

    def __init__(self):
        self.head = None

    def addAtHead(self, val):
        node = Node(val)
        node.next = None
        node.prev = None
        self.head = node


    