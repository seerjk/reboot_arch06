#!/usr/bin/env python

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def setup(n):
    head = Node(0, None)
    curr = head
    for i in range(1, n):
        node = Node(i, None)
        curr.next = node
        curr = node
    return head

def run(node):
    sum = 0
    while node:
        sum += node.val
        node = node.next
    print sum
