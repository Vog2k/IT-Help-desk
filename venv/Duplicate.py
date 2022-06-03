# Timothy L
# IT Help Desk
# Start Date 30/5/22 7am
# Update 02/06/22 12:57pm
from Dup2 import Tickets
import datetime
import random

                            # To Do
"""
The first two characters of the staff ID,followed by the hexadecimal
representation of the ticket number, followed by a hexadecimal representation
of the first three characters of the timestamp.

1.Internal Tickets’ ticket number should be assigned
automatically using the counter static field plus 2000.

2.There are two ways of submitting an internal ticket: either by providing staff ID,
ticket creator name, contact email and the description of the issue or only by providing------ DONE------
staff ID and the description of the issue

3.For your information, StaffID is made up of the employee’s name followed----- DONE----- IN ASSIGNMENT
by the first letter of the employee’s surname.



---------------------------Responding to tickets------------------------

If the ticket’s description of the issue contains the words “Password Change”,
the new password should be generated following the rule: The first two characters of the staff ID -----NEED HELP WITH---
followed by the hexadecimal representation of the ticket number
followed by a hexadecimal representation of the first three characters of the timestamp.

You may find the following link useful:
How to convert between hexadecimal strings and numeric types (C# Programming Guide)

There should be an option after the ticket has been 
submitted to respond to a ticket by providing a feedback response. --------DONE----

-----------------------------Statistics--------------

There should be a way to keep track of the number of tickets submitted,
number of resolved tickets and number of open tickets, and a way to display those statistics to the console.

If the staff member has submitted the “Password change” request,
after the new password is generated and the ticket’s response has been updated,
the ticket should close, with the number of closed tickets increased and the number
of open tickets reduced by 1. Ticket’s status should be changed to “Closed”.

Once a member of the IT department provides the response to a ticket, the ticket should close,
with the number of closed tickets increased and the number of open tickets reduced by 1.
Ticket’s status should be changed to “Closed”.

There should be an option for the IT department to reopen the ticket. At this point the
number of open tickets should be increased and the number of closed tickets should be reduced by 1.
Ticket’s status should be changed to “Reopened”



-------------Technical Requirements-------------------

The Ticket class should contain common ticket information in the Ticket class. [X]

The Ticket class should also have methods allowing the IT team to respond to the tickets,
specifically resolve, reopen and provide a response to the ticket.

The object creation of Ticket type should be performed through the use of constructors. [X]

The Ticket class should contain a method for resolving password change requests.
As well as calling the method that would generate the new password,
it should set up a response for the ticket and change the ticket status to closed. [X]

There should be a method to print information for all the ticket objects
(Hint: research and use List<Ticket>).

The TicketStats class should contain information on ticket statistics.
Variables for storing statistics on tickets created, tickets opened and tickets closed
should be encapsulated and set to a default value of 0. There should also be a method,
returning a string value that displays the statistics information. NEED TO ADD THIS---------------

The PasswordGenerator class should have a static method that generates a password as per
the client requirements, based on the ticketNumber and staffID parameters provided.
This method should be called if the user’s ticket issue description contains the
phrase “Password Change”.

The main class, containing the Main method:



"""

def Welcome():  # Sign in options

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
            login2 = input("New Password: \n")
            file = open(login1 + ".txt", "r") #Need help changing a password
            data = file.readline()
            file.close()
            if data == login1 + ":" + login2:
                print("Welcome", " " + login1)
                break
            print("Incorrect username or password.")

Welcome()

def Home_page():    # Ticket options

    print()
    print("0. Ticket information")
    print("1. Change password")
    print("2. Chang email")
    print("3. Lost equipment")
    print("4. Describe your problem")
    print("5. To quit")

    print("--------------------------")

    option = input("Please enter a number from the following list: ")

    if option == "0":

        tkt_1 = Tickets("Ticket status : ", "Ticket number: 2000", "Ticket creator: Timothy", "ID number: TL5991",
                        "Email:  Tim.leatau@whitecliffe.com", "Chosen option:  View ticket")

        print()
        print("-Current Tickets displayed-\n") # Do not touch
        print("-------------TICKET-------------")
        print(tkt_1.status, tkt_1.Issued()) # Determines weather or not the ticket has been filled or not
        print(tkt_1.ticket_number) # Fixed number starting from 2000
        print(tkt_1.ticket_creator) # Assign persons name
        print(tkt_1.staff_id) #First character of the first and last name
        print(tkt_1.email) # Fist and last name together
        print(tkt_1.problem) # Assigned to ticket option
        print("-------------END OF TICKET-------------\n")

        Home_page()

    if option == "1":
        print()
        input("Please enter your Id or Username: ")
        print("Please enter 'change'\n")
        Welcome()
        tkt_1 = Tickets("Ticket status : ", "Ticket number: 2000", "Ticket creator: Timothy", "ID number: TL5991",
                        "Email:  Tim.leatau@whitecliffe.com", "Chosen option:  Change password")

        print()

        print("-Current Tickets displayed-\n")
        print("-------------TICKET-------------")
        print(tkt_1.status, tkt_1.Issued()) # Determines weather or not the ticket has been filled or not
        print(tkt_1.ticket_number) # Fixed number starting from 2000
        print(tkt_1.ticket_creator) # Assign persons name
        print(tkt_1.staff_id) #First character of the first and last name
        print(tkt_1.email) # Fist and last name together
        print(tkt_1.problem) # Assigned to ticket option
        print("-------------END OF TICKET-------------\n")


        Home_page()
        if option >= "1":
            x = input("Add feedback: ") # MOVE
            print(x)

    elif option == "2":

        tkt_2 = Tickets("Ticket status : ", "Ticket number: 2000", "Ticket creator: Timothy", "ID number: TL5991",
                        "Email:  Tim.leatau@whitecliffe.com", "Chosen option:  Change password")
        print()

        print("-Current Tickets displayed-\n")
        print("-------------TICKET-------------\n")
        print(tkt_2.status, tkt_2.Issue()) # Determines weather or not the ticket has been filled or not
        print(tkt_2.ticket_number) # Fixed number starting from 2000
        print(tkt_2.ticket_creator) # Assign persons name
        print(tkt_2.staff_id) #First character of the first and last name
        print(tkt_2.email) # Fist and last name together
        print(tkt_2.problem) # Assigned to ticket option
        print("-------------END OF TICKET-------------")

    elif option == "3":

        tkt_2 = Tickets("Ticket status : ", "Ticket number: 2000", "Ticket creator: Timothy", "ID number: TL5991",
                        "Email:  Tim.leatau@whitecliffe.com", "Chosen option:  Change password")
        print()

        print("-Current Tickets displayed-\n")
        print("-------------TICKET-------------")
        print(tkt_2.status, tkt_2.Issue()) # Determines weather or not the ticket has been filled or not
        print(tkt_2.ticket_number) # Fixed number starting from 2000
        print(tkt_2.ticket_creator) # Assign persons name
        print(tkt_2.staff_id) #First character of the first and last name
        print(tkt_2.email) # Fist and last name together
        print(tkt_2.problem) # Assigned to ticket option
        print("-------------END OF TICKET-------------\n")

    elif option == "4":

        tkt_2 = Tickets("Ticket status : ", "Ticket number: 2000", "Ticket creator: Timothy", "ID number: TL5991",
                        "Email:  Tim.leatau@whitecliffe.com", "Chosen option:  Change password")
        print()

        print("-Current Tickets displayed-\n")
        print("-------------TICKET-------------")
        print(tkt_2.status, tkt_2.Issue()) # Determines weather or not the ticket has been filled or not
        print(tkt_2.ticket_number) # Fixed number starting from 2000
        print(tkt_2.ticket_creator) # Assign persons name
        print(tkt_2.staff_id) #First character of the first and last name
        print(tkt_2.email) # Fist and last name together
        print(tkt_2.problem) # Assigned to ticket option
        print("-------------END OF TICKET-------------\n")

    elif option == "5":
        print("Now exiting") # break

    else:
        Home_page()


print("---------------------------")

Home_page()
















