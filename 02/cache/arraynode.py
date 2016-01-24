#!/usr/bin/env python

class Node:
    def __init__(self, val):
        self.val = val

def setup(n):
    l = range(n)
    for i in range(0, n):
        l[i] = Node(i)
    return l

def run(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i].val
    print sum
