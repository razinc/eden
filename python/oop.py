######################################################
# Tutorial 1                                         #
# Classes and Instances                              #
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&t=685s #
######################################################

# attributes    - adjectives of a class
# method        - verb of a class

# defining class
class Employee:

    raise_amount = 1.4
    no_of_emps = 0

    # constructor
    def __init__(self, firstn, lastn, pay):
        self.firstn = firstn
        self.lastn = lastn
        self.email = f"{firstn}.{lastn}@company.com"

        Employee.no_of_emps += 1

    def full_name(self):
        return f"{self.firstn} {self.lastn}"

    def apply_raise(self):
        # self.raise_amount != Employee.raise_amount
        self_pay = int(self.pay * self.raise_amount)        

emp_1 = Employee("Bruce", "Wayne", 5000)
emp_2 = Employee("Clark", "Kent", 200)

# print attribute
print(emp_1.firstn)
print(emp_2.email)

# print method
print(emp_1.full_name())
print(Employee.full_name(emp_2))

####################################################################################################
# Tutorial 2                                                                                       # 
# Class Variable                                                                                   #
# https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=3&t=0s #
####################################################################################################

# variable of class
print(Employee.raise_amount)

# variable of instance
print(emp_1.raise_amount)

# changing variable of instance
emp_2.raise_amount = 1.5
print(Employee.raise_amount)
print(emp_1.__dict__)
print(emp_1.raise_amount)
print(emp_2.__dict__)
print(emp_2.raise_amount)

print(Employee.no_of_emps)
