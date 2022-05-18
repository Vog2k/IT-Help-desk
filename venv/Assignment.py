import random
import uuid
import datetime

"""
def Ticket():
    pass

class Employee:

   def __init__(self, first, last, id):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@whitecliffe"
   def fullname(self):
        return '{} {}'.format(self.first, self.last)
   pass
"""
def main ():

    print()
    first = input("Enter first name - :")
    last = input("Enter last name - :")
    email = first + "." + last + "@whitecliffe"
    id = "15186146"
    if first + last :
        print("ID:" + first + last + id)
    else:
        print()
        print("Please enter a valid name")


"""
class ID():

    def i_D(self):
        self.id = id

ran_id = uuid.uuid4()
print("Your new ID is :" + str(ran_id))
input("Please copy & paste your code here")

pass


class lecturer(Employee):


    Employee()
    print(Employee.fullname(emp_1))

ID = int(input("Please enter ID number here :"))

print("1. Lost or misplaced device\n"
      "2. Damaged property\n"
      "3. New ID\n")
print("Please choose an option")
option = int(input())

pass
"""