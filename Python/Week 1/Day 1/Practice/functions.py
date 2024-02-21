def countdown(n):
    return list(range(n, -1, -1))
print(countdown(5))


def print_and_return(lst):
    print(lst[0])
    return lst[1]
print(print_and_return([1,2]))


def first_plus_length(lst):
    return lst[0] + len(lst)
print(first_plus_length([1,2,3,4,5]))


def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    else:
        greater_values = [value for value in lst if value > lst[1]]
        print(f"There are {len(greater_values)} values greater than the second value.")
        return greater_values
print(values_greater_than_second([5,2,3,2,1,4])) 
print(values_greater_than_second([3]))


def length_and_value(size, value):
    return [value] * size
print(length_and_value(4,7)) 
print(length_and_value(6,2))