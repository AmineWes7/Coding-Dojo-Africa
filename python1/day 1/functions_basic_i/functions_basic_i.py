#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())  # 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())  # Error

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())  # 5

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())  # 5

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)  #  5, None

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))  # Error

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))  # "25"

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())  # 100, 10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))  #  7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))  #  14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))  #  21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))  #  8

#11
b = 500
print(b)  # 500
def foobar():
    b = 300
    print(b)  # 300
print(b)  # 500
foobar()
print(b)  #  500

#12
b = 500
print(b)  # : 500
def foobar():
    b = 300
    print(b)  #300
    return b
print(b)  #  500
foobar()
print(b)  # 500

#13
b = 500
print(b)  #  500
def foobar():
    b = 300
    print(b)  # 300
    return b
print(b)  # 500
b=foobar()
print(b)  #  300

#14
def foo():
    print(1)  #  1
    bar()
    print(2)  #  2
def bar