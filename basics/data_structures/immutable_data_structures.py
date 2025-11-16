# here's the list of built in immutable data structures in python

tuple_example = (1, 2, 3)

try:
    tuple_example[0] = 99
except TypeError as e:
    print(e)