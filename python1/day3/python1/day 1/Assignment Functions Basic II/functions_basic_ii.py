def countdown(n):
    return list(range(n, -1, -1))

print(countdown(5))  # [5, 4, 3, 2, 1, 0]
#-----------------------------------------------------------------
def print_and_return(lst):
    print(lst[0])
    return lst[1]

print(print_and_return([1, 2]))  # 1, 2
#-----------------------------------------------------------------
def first_plus_length(lst):
    return lst[0] + len(lst)

print(first_plus_length([1, 2, 3, 4, 5]))  # 6
#-----------------------------------------------------------------
def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    second_value = lst[1]
    new_list = [x for x in lst if x > second_value]
    print(len(new_list))
    return new_list

print(values_greater_than_second([5, 2, 3, 2, 1, 4]))  #  3, then [5, 3, 4]
print(values_greater_than_second([3]))  # False
#-----------------------------------------------------------------
def length_and_value(size, value):
    return [value] * size

print(length_and_value(4, 7))  #[7, 7, 7, 7]
print(length_and_value(6, 2))  #[2, 2, 2, 2, 2, 2]