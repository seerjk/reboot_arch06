#!/usr/bin/env python

import timeit

setup = '''
import arraynode
import listnode
'''

print timeit.timeit(
    "arraynode.run(l)", 
    setup="import arraynode;l = arraynode.setup(1000000)", 
    number=1)

print timeit.timeit(
    "listnode.run(head)", 
    setup="import listnode;head = listnode.setup(1000000)",
    number=1)

