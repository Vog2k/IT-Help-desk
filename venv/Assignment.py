# Timothy L
# IT Help Desk
# Start Date 30/5/22 7am

import random
import uuid
import datetime
# from Staff import work




def SignIn():
    print("Welcome")
    status = input("Do you currently have an account ?\nPlease enter 'Y' for yes or 'N' for no: ")
    if status == "Y": # Requires the user to enter Y or N
        old_user() # If the user is old this should send them straight to entering their ID
    else:
        if status == "N": #If the user is new then this part should send them straight to the register page
            Register()

def Space(): # Dry
    print()

def Register():


    Space()
    first_name = input("Enter first name - ")
    Space()
    last_name = input("Enter last name - ")
    Space()

    password = input("Please enter your new password: ")
    Space()

    first_char = first_name[0]
    last_char = last_name[0]
    full_name = first_name + " " + last_name
    first_two = first_char + last_char
    email = first_name + "." + last_name + "@whitecliffe"
    ram_id = random.randint(1000000, 5000000)  # Needs randomized number later
    internal_id = first_two + str(ram_id)



    if first_name + last_name == first_name + last_name:
        print("Thank you for registering ", full_name)
        print("Here is you're new ID")
        print("Work email is: ", email)
        print("ID:", internal_id)
        print("Password: ", password)
        print()
        SignIn()

    else:
        if first_name != []:
            if last_name != []:
                print("Error please enter you're name")
        Register()





def old_user():

    Sign_in = input("Please enter your ID# ")
    if Sign_in == Sign_in: #NEEDS A LIST OF IDs
        print()
        home()
    else:
     if Sign_in != Sign_in: #NEEDS A LIST OF IDs
         input("Error Please enter correct ID")
    old_user()



def home():
    print("Login successful")


    print("Welcome\n")

    print("1. Change password")
    print("2. Chang email")
    print("3. Lost equipment")
    print("4. Lost connection to the internet")
    print("5. Equipment not working")
    print("6. Error")

    Space()
    num = input("Please enter a number: ")

    tkt_1 = "1"
    tkt_2 = "2"
    tkt_3 = "3"
    tkt_4 = "4"
    tkt_5 = "5"
    tkt_6 = "6"



    if num == "1":
        SignIn_Password_reset(tkt_1)
    else:
        print("Error please enter a number")
        home()

    if tkt_2 == "2":
        SignIn_Password_reset(tkt_1)
    else:
        print("Error please enter a number")
        home()

    if tkt_2 == "3":
        SignIn_Password_reset(tkt_1)
    else:
        print("Error please enter a number")
        home()

    if tkt_2 == "4":
        SignIn_Password_reset(tkt_1)
    else:
        print("Error please enter a number")
        home()

    if tkt_2 == "5":
        SignIn_Password_reset(tkt_1)
    else:
        print("Error please enter a number")
        home()

    if tkt_2 == "6":
        SignIn_Password_reset(tkt_1)
    else:
        print("Error please enter a number")
        home()





# Later on
"""def SignIn_Password_reset(tkt_1):

    if needed == :
        new_password
    else:
        print("Please enter a valid password")
        SignIn_Password_reset(tkt_1)

needed = input("Please enter your ID or your name")
new_password = input("Please enter a new password")"""

def description(tkt_6):
    des = input("Please enter your situation")
    if des == "":
        home()


def print_tkt(full_name):

    Ticket_status_open = "Open"
    Ticket_status_closed = "Closed"
    if Ticket_status == '1''2''3''4''5''6':
        print(Ticket_status_open)
    else:
        print(Ticket_status_closed)

    #Ticket_number = /// Make this start from 2000

    Ticket_creator = full_name







def main():
    if SignIn() == "Y":
        old_user()
    else:
        if SignIn() == "N":
            Register()
    home()
    if home == 1:
        SignIn_Password_reset(tkt_1)





main()

