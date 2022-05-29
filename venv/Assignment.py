import random
import uuid
import datetime

def SignIn():
    Start = print("Welcome")
    status = input("Do you currently have an account ?\nPlease enter 'Y' for yes or 'N' for no: ")
    if status == "Y": # Requires the user to enter Y or N
        old_user() # If the user is old this should send them staright to entering their ID
    else:
        if status == "N": #If the user is new then this part should send them straight to the register page
            Register()

def Register():

    print()
    first_name = input("Enter first name - ")
    print()
    last_name = input("Enter last name - ")
    print()

    first_char = first_name[0]
    last_char = last_name[0]
    first_two = first_char + last_char
    email = first_name + "." + last_name + "@whitecliffe"
    ram_id = random.randint(1000000, 5000000) #Needs randomized number later
    internal_id = first_two + str(ram_id)


    if first_name + last_name == first_name + last_name:
        print("Here is you're new ID")
        print("ID:", internal_id)
        SignIn()

    else:
        if first_name != []:
            if last_name != []:
                print("Error please enter you're name")
        Register()




def old_user():
    Sign_in = input("Please enter your ID# ")
    if Sign_in == Sign_in: #NEEDS A LIST OF IDs
        print("Welcome")
        Homr()
    else:
     if Sign_in != Sign_in: #NEEDS A LIST OF IDs
         input("Error Please enter correct ID")
    old_user()



def home():
    print("Welcome\n")


    tkt_1 = print("1. Change password")
    tkt_2 = print("2. Chang email")
    tkt_3 = print("3. Lost equipment")
    tkt_4 = print("4. Lost connection to the internet")
    tkt_5 = print("5. Equipment not working")
    tkt_6 = print("6. Error")

    if tkt_1 == tkt_1:

def SignIn_Password_reset(tkt_1):
    old_password = input("Please enter your current password")
    new_password = input("Please enter a new password")
    if old_password == old_password:
        new_password()




def main():
    if SignIn() == "Y":
        old_user()
    else:
        if SignIn() == "N":
            Register()








main()

