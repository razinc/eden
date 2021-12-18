# Basic Operation

## String Splitting
```python
my_string = "this is a string"
my_list = list(my_string)
print(my_list)
# ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g']
```

# Sorting

```python
my_list = test_list = ["dir_79", "dir_8", "dir_80"]
my_list.sort(key = lambda x:int(x.replace("dir_", "")))
print(my_list)
# ['dir_8', 'dir_79', 'dir_80']
```

# List Comprehension

## Create a List
```python
nums = [i for i in range(10)]
print(nums)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odds = [i for i in nums if i % 2 != 0]
print(odds)
# [1, 3, 5, 7, 9]
```

## List Check
```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if any([True if num % 2 != 0 else False for num in nums]):
    print("List contains odd number")
else:
    print("List doesn't contain odd number")
# List contains odd number
```
