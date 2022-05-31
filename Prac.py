import random


class Employee:  # Parent Class

    def __init__(self):
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
print(Employee, "Parent class")
print(Test.)
