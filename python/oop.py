####################################################################################################
# Tutorial 1                                                                                       #
# Classes and Instances                                                                            #
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=2&t=0s #
####################################################################################################

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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # classmethod as alternative constructor
    @classmethod
    def from_str(cls, new_emp):
        firstn, lastn, pay = new_emp.split("-")
        return cls(firstn, lastn, pay)

    @staticmethod
    def is_working_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

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

####################################################################################################
# Tutorial 3                                                                                       # 
# classmethods & staticmethods                                                                     #
# https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4&t=0s #
####################################################################################################

# regular method    - pass self
# classmethod       - pass class
# staticmethod      - no relation to instance or class

Employee.set_raise_amt(1.05)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_3 = Employee.from_str("Hal-Jordan-500")
print(emp_3.email)

import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_working_day(my_date))
