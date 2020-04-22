#########################################################
# 1. https://www.youtube.com/watch?v=ZDa-Z5JzLYM&t=685s #
#########################################################

# attributes    - adjectives of a class
# method        - verb of a class

# defining class
class Employee:

    # constructor
    def __init__(self, firstn, lastn, pay):
        self.firstn = firstn
        self.lastn = lastn
        self.email = f"{firstn}.{lastn}@company.com"

    def full_name(self):
        return f"{self.firstn} {self.lastn}"    

emp_1 = Employee("Bruce", "Wayne", 5000)
emp_2 = Employee("Clark", "Kent", 200)

# print attribute
print(emp_1.firstn)
print(emp_2.email)

# print method
print(emp_1.full_name())
print(Employee.full_name(emp_2))
