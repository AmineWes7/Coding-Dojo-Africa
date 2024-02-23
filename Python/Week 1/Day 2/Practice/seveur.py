def update_values(x, index1, index2, new_value):
    x[index1][index2] = new_value
    return x
x = [ [5,2,3], [10,8,9] ]
x = update_values(x, 1, 0, 15)
print(x)  # Output: [ [5,2,3], [15,8,9] ]

def iterateDictionary(some_list):
    for dictionary in some_list:
        for key, value in dictionary.items():
            print(f"{key} - {value}")
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{len(value)} {key.upper()}")
        for item in value:
            print(item)
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)