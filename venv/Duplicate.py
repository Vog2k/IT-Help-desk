#OOP ASSIGNMENT
from Dup2 import Tickets
import datetime
import random

def Welcome():

    print("Welcome...")
    welcome = input("Do you have an account? y/n: ")
    if welcome == "n":
        while True:
            username = input("Enter a username :")
            print()
            password = input("Enter a password :")
            print()
            password1 = input("Confirm password :")
            if password == password1:
                file = open(username + ".txt", "w")
                file.write(username + ":" + password)
                file.close()
                welcome = "y"
                break
            print("Passwords do NOT match!")

    if welcome == "y":
        while True:
            login1 = input("Login: ")
            print()
            login2 = input("Password: ")
            file = open(login1 + ".txt", "r")
            data = file.readline()
            file.close()
            if data == login1 + ":" + login2:
                print("Welcome", " " + login1)
                break
            print("Incorrect username or password.")

    if welcome == "change":
        while True:
            login1 = input("Login: ")
            print()
            login2 = input("New Password: ")
            file = open(login1 + ".txt", "r") #Need help changing a password
            data = file.readline()
            file.close()
            if data == login1 + ":" + login2:
                print("Welcome", " " + login1)
                break
            print("Incorrect username or password.")

def Home_page():

    print()
    print("1. Change password")
    print("2. Chang email")
    print("3. Lost equipment")
    print("4. Describe your problem")
    print("5. To quit")

    print("--------------------------")

    option = input("Please enter a number from the following list: ")

    if option == "1":
        print()
        print("Please enter 'change'")
        Welcome()
        tkt_1 = Tickets("Ticket status : ", "Ticket number: 2000", "Ticket creator: Timothy", "ID number: TL5991",
                        "Email:  Tim.leatau@whitecliffe.com", "Chosen option:  Change password")
        print()
        print("-Current Tickets displayed-\n")
        print(tkt_1.status, tkt_1.Issued()) # Determines weather or not the ticket has been filled or not
        print(tkt_1.ticket_number) # Fixed number starting from 2000
        print(tkt_1.ticket_creator) # Assign persons name
        print(tkt_1.staff_id) #First character of the first and last name
        print(tkt_1.email) # Fist and last name together
        print(tkt_1.problem) # Assigned to ticket option

        Home_page()

    elif option == "2":

        tkt_2 = Tickets("Ticket status : ", "Ticket number: 2000", "Ticket creator: Timothy", "ID number: TL5991",
                        "Email:  Tim.leatau@whitecliffe.com", "Chosen option:  Change password")
        print()
        print("-Current Tickets displayed-\n")
        print(tkt_2.status, tkt_2.Issue()) # Determines weather or not the ticket has been filled or not
        print(tkt_2.ticket_number) # Fixed number starting from 2000
        print(tkt_2.ticket_creator) # Assign persons name
        print(tkt_2.staff_id) #First character of the first and last name
        print(tkt_2.email) # Fist and last name together
        print(tkt_2.problem) # Assigned to ticket option

    elif option == "3":

        tkt_2 = Tickets("Ticket status : ", "Ticket number: 2000", "Ticket creator: Timothy", "ID number: TL5991",
                        "Email:  Tim.leatau@whitecliffe.com", "Chosen option:  Change password")
        print()
        print("-Current Tickets displayed-\n")
        print(tkt_2.status, tkt_2.Issue()) # Determines weather or not the ticket has been filled or not
        print(tkt_2.ticket_number) # Fixed number starting from 2000
        print(tkt_2.ticket_creator) # Assign persons name
        print(tkt_2.staff_id) #First character of the first and last name
        print(tkt_2.email) # Fist and last name together
        print(tkt_2.problem) # Assigned to ticket option

    elif option == "4":

        tkt_2 = Tickets("Ticket status : ", "Ticket number: 2000", "Ticket creator: Timothy", "ID number: TL5991",
                        "Email:  Tim.leatau@whitecliffe.com", "Chosen option:  Change password")
        print()
        print("-Current Tickets displayed-\n")
        print(tkt_2.status, tkt_2.Issue()) # Determines weather or not the ticket has been filled or not
        print(tkt_2.ticket_number) # Fixed number starting from 2000
        print(tkt_2.ticket_creator) # Assign persons name
        print(tkt_2.staff_id) #First character of the first and last name
        print(tkt_2.email) # Fist and last name together
        print(tkt_2.problem) # Assigned to ticket option

    elif option == "5":
        print("Now exiting") # break

    else:
        Home_page()


print("---------------------------")

Home_page()
















