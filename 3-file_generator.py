import sys

def csv_reader(file_name):
    file = open(file_name, 'r')
    result = file.read().split('\n')
    return result

def csv_reader_generator(file_name):
    for row in open(file_name, 'r'):
        yield row

def get_number_lines(data_reader):
    row_count = 0
    for row in data_reader:
        row_count += 1

    return row_count

# Test
print(f"{get_number_lines(csv_reader('random.csv'))} lines")
print(f"{get_number_lines(csv_reader_generator('random.csv'))} lines")

# Memory
print(f"{sys.getsizeof(csv_reader('random.csv'))} bytes for list")
print(f"{sys.getsizeof(csv_reader_generator('random.csv'))} bytes for generator")




