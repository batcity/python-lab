# here's the list of built in immutable data structures in python

# tuples
tuple_example = (1, 2, 3)

try:
    tuple_example[0] = 99
except TypeError as e:
    print(e)
    

# frozen set    
frozen_set_example = frozenset([1,2,3])

try:
    frozen_set_example.add(5)
except AttributeError as e:
    print(e)
    
    
# String
word = "hello"
print("memory address of the original string:", id(word))   # memory address (identity)

word = word + " world"
print("memory address of the modified string:", id(word))   # different address