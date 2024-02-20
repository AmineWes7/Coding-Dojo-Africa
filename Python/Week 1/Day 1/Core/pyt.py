# Basic - Print all integers from 0 to 150
for i in range(151):
    print(i)
for i in range(5, 1001, 5):
    print(i)
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)
total = 0
for i in range(1, 500001, 2):
    total += i
print(total)
for i in range(2018, -1, -4):
    print(i)
