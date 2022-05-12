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

try:
    odd_iterator = OddIterator(5)
    print(next(odd_iterator))
    print(next(odd_iterator))
    print(next(odd_iterator))
    print(next(odd_iterator))
    print(next(odd_iterator))
except StopIteration:
    print('No value to next')
