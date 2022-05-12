def simple_generator_func():
    yield 1
    yield 2
    yield 3
     
def simple_generator_expr():
    return (i for i in range(10))

def odd_generator(max=10):
    number = 1
    while (number < max):
        yield number
        number += 2

odd_numbers = odd_generator(20)
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))


# print(type(simple_generator()))

# data = (simple_generator())
# print(next(data))
# print(next(data))


# data_2 = simple_generator_bracket()
# print(type(data_2))
# print(next(data_2))
# print(next(data_2))
# print(next(data_2))