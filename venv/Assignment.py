import random
import uuid
import datetime

def SignIn():
    Start = print("Welcome")
    status = input("Do you currently have an account ?\nPlease enter 'Y' for yes or 'N' for no: ")
    if status == "y" + "Y": # Requires the user to enter Y or N
        old_user() # If the user is old this should send them staright to entering their ID
    else:
        if status == "N" + "n": #If the user is new then this part should send them straight to the register page
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

    else:
        if first_name != []:
            if last_name != []:
                print("Error please enter you're name")
        Register()



def old_user():
    Sign_in = input("Please enter your ID# ")
    if Sign_in == Sign_in: #NEEDS A LIST OF IDs
        print("Welcome")
    else:
     if Sign_in != Sign_in: #NEEDS A LIST OF IDs
         input("Error Please enter correct ID")
    old_user()







def main():
    if SignIn() == True:
        old_user()
    else:
        if SignIn() == False:
            Register()





main()

