# create a list
nums = [i for i in range(10)]
print(nums)

# with conditional
odds = [i for i in nums if i % 2 != 0]
print(odds)

# check if any element in a list satisfy a condition
if any([True if num % 2 != 0 else False for num in nums]):
    print("List contains odd number")
else:
    print("List doesn't contain odd number")

# check if substring in string in list
words = ["apple", "two, three"]
if any([True if "ple" in word else False for word in words]):
    print("List contains \"ple\"")
else:
    print("List does not contains \"ple\"")
    
