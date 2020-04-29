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
        self.pay = pay
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

    # good practice: print message to recreate object
    def __repr__(self):
        return f"Employee({self.firstn}, {self.lastn}, {self.pay})"

    # print redeable message
    def __str__(self):
        return f"{self.full_name()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    @property
    def email_dec(self):
        return f"{self.firstn}.{self.lastn}@company.com"

    @email_dec.setter
    def email_dec(self, email):
        self.firstn, self.lastn = email.strip("@company.com").split(".")

    @email_dec.deleter
    def email_dec(self):
        print("Delete First Name & Last Name")
        self.firstn = None
        self.lastn = None


class Developer(Employee):

    # overwrite parent's attribute
    raise_amount = 1.5

    # add new attribute to constructor
    def __init__(self, firstn, lastn, pay, prog_lang):
        super().__init__(firstn, lastn, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, firstn, lastn, pay, employees = None):
        super().__init__(firstn, lastn, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def del_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f"--> {emp.full_name()}")                


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

####################################################################################################
# Tutorial 4                                                                                       # 
# Inheritance - Creating Subclasses                                                                #
# https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=5&t=0s #
####################################################################################################

emp_4 = Developer("Oliver", "Queen", 2000, "C++")
print(emp_4.email)
print(emp_4.prog_lang)

mngr_1 = Manager("Barry", "Allen", 5500, [emp_1])
print(mngr_1.email)
mngr_1.print_emps()
mngr_1.add_emp(emp_2)
mngr_1.print_emps()
mngr_1.del_emp(emp_1)
mngr_1.print_emps()

print(isinstance(mngr_1, Manager))
print(issubclass(Manager, Developer))

####################################################################################################
# Tutorial 5                                                                                       # 
# Special Methods (Dunder Methods)                                                                 #
# https://www.youtube.com/watch?v=3ohzBxoFHAY&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6&t=0s #
####################################################################################################

print(emp_1)
print(repr(emp_1))
print(emp_1.__repr__())
print(str(emp_1))
print(emp_1.__str__())

print(emp_1 + emp_2)

####################################################################################################
# Tutorial 6                                                                                       # 
# Decorator (Getters, Setters, Deleters)                                                           #
# https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=7&t=0s #
####################################################################################################

emp_1.firstn = "Thomas"
print(emp_1.firstn)
print(emp_1.email)
print(emp_1.email_dec)

emp_1.email_dec = "Martha.Wayne@compay.com"
print(emp_1.firstn)
print(emp_1.lastn)

del emp_1.email_dec
print(emp_1.firstn)
print(emp_1.lastn)
