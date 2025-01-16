#How to do a profile in python

import cProfile

def sum():
    print(1,3)
cProfile.run('sum()')