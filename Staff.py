import random


class Employee:  # Parent Class

    def __init__(self, firstName, lastName, password):  # Defines your variables
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName + '.' + lastName + "@Whitecliffe.com"
        self.password = password

    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def emp_pwd(self):
        self.password = input("Please enter a password")


emp_1 = Employee(input("First"), input("Last"), input("Password"))
emp_2 = Employee(input("First1"), input("Last1"), input("Password1"))

print(Employee.fullname())
print(emp_1.email)


"""class Employee:  # Parent Class

    def __init__(self, ):
        self.name = "no"
        self.ID()

    def ID(self):
        print("Yes")


class Ticket(Employee):  # Child Class
    def __init__(self):
        super().__init__()
        self.name = "fuck"
        self.__password = "passwords cunt" # Double underscore means the user cant see it


Test = Ticket()
print(Test.name, "Child class")
print(Employee, "Parent class")"""

