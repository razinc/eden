person = {"name": "Ali", "age": 18, "phone": 123456}

# get all keys
print(person.keys())

# get all values
print(person.values())

# get both keys & values
print(person.items())

# loop dict
for key, value in person.items():
    print(key, value)

# sort dict based on value
from collections import OrderedDict
from operator import getitem
d = {"Apple" : {"Colour" : "Red", "Count" : 23},
    "Grape" : {"Colour" : "Purple", "Count" : 11}, 
    "Melon" : {"Colour" : "Green", "Count" : 34}}
d_mark_sort = OrderedDict(sorted(d.items(), key = lambda x: getitem(x[1], "Count")))
print(d_mark_sort)
