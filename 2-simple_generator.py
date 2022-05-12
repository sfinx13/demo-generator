# 1 - Create generator with yield statement
print("1 - Create generator with yield statement")
def simple_generator_func():
    yield 1
    yield 2
    yield 3

print(type(simple_generator_func()))
data_generator = simple_generator_func()
print(next(data_generator))
print(next(data_generator))
print(next(data_generator))


# 2 - Create generator with parenthesis     
print("2 - Create generator with parenthesis")
def simple_generator_expr():
    return (i for i in range(10))

print(type(simple_generator_expr()))
data_generator = (simple_generator_expr())
print(next(data_generator))
print(next(data_generator))


# 3 - Create a generator which handle odd numbers
print("3 - Create a generator which handle odd numbers")

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
