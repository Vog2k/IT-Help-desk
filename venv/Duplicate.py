def Welcome():

    print("Welcome...")
    welcome = input("Do you have an account? y/n: ")
    if welcome == "n":
        while True:
            username = input("Enter a username :")
            password = input("Enter a password :")
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
            login2 = input("Password: ")
            file = open(login1 + ".txt", "r")
            data = file.readline()
            file.close()
            if data == login1 + ":" + login2:
                print("Welcome" + login1)
                break
            print("Incorrect username or password.")

Welcome()

def Home_page():
    print("Welcome")# Add username


    print("1. Change password")
    print("2. Chang email")
    print("3. Lost equipment")
    print("4. Lost connection to the internet")
    print("5. Equipment not working")
    print("6. Error")

    print()

    num = input("Please enter a number: ")

    if num == 1:
        ticket


Home_page()

class ticket:

    def __init__(self, ticket_status, ticket_number, tkt_creator, staff_id, email, problem):
        self.tkt_stat = tkt_stat
        self.tkt_num = tkt_num
        self.tkt_cre = tkt_cre
        self.staff_id = staff_id
        self.email = email
        self.problem = problem

    def get_Ticket(self):
        print(f"Ticket Status -{self.tkt_stat}\n")
        print(f"Ticket Number -{self.tkt_num}\n")
        print()



        ticket_status = "Open/closed"
        if problem == "[]":
            print("Open")
        else:
            print("Closed")


Ticket = ticket
Ticket.get_Ticket()




