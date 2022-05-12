---
marp: true
title: Generator with yield statement and expression
theme: gaia
_class: lead
paginate: true
color: black
---

# Generator : *yield statement*

Demo made with python language

----
# Overview

* What is a generator ?

* Can we should talk iterator first ?

* Why you should use it ?

* How to create a generator ?
    - `yield` statement
    - `()` expression

* Profiling Generator Performance.
---

# What is a generator ?

Introduced with [PEP 255](https://peps.python.org/pep-0255/), generator are a special kind of object implementing iterator

An iterator object implements thses methods:

| Methods        |   Description           |
----------|--------------|
```__iter__()```| Return the iterator object itself  |
```__next__()```| Return the next item from the iterator |
raise ```StopIteration```| If there are no further items, raise the StopIteration exception |

This a an object that you can loop over like a list with for, while loop

---

# An iterator: example

```python
class OddIterator():
    def __init__(self, max=1):
        self.max = max
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        if (self.number > self.max):
            raise StopIteration

        number = self.number
        self.number += 2
        return number
```

---

# An iterator: call iterator

Using next(), Python calls ```.__next__()``` method from object iterator.

```python
try:
    odd_iterator = OddIterator(5)
    print(next(odd_iterator))
    print(next(odd_iterator))
    print(next(odd_iterator))
    print(next(odd_iterator))
    print(next(odd_iterator))
except StopIteration:
    print('No value to next')
```

Instead of using a for loop, we call next() on the iterator object 


---

# Why you should use it ?

* Because you have to work with data streams or large files, like CSV files.

* Because you have to deal with infinite sequence cause your computer memory is finite.

* Because you have a complex function that needs to maintain an internal state every time it’s called.
---

# How to create a generator 1/2 ?

To create a generator you have to use `yield` statement.

```python
def generator_func():
    yield 1
    yield 2

data = generator_func()
print(next(data))
# 1
```
*a `return` statement terminates a function, `yield` statement pauses the function saving its states and later continues from there on successive calls*

---
# How to create a generator 2/2?

Generators can be easily created on the fly using generator expression

```python
def simple_generator_expr():
    return (i for i in range(10))
```

The syntax is similar to that of a list in Python. But the square brackets `[]` are replaced with round parentheses `()`.

---

# Profiling Generator Performance
In the slide before, we mention generator is a great way to optimize memory

So let's profile with `sys.getsizeof()`

```python
import sys
nums_squared_list = [i * 2 for i in range(10000)]
sys.getsizeof(nums_squared_lc)
# 87624 bytes

nums_squared_generator = (i * 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))
# 120 bytes
```
---
# Conclusion

You have learned about generator functions and generator expressions by knowing the benefits

## Links
* https://docs.python.org/3/glossary.html#term-generator
* https://docs.python.org/3/library/stdtypes.html#iterator-types
* https://docs.python.org/3/library/functions.html#next
* https://wiki.python.org/moin/Generators
* https://peps.python.org/pep-0255/ 
