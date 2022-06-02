import random


class Tickets:

    def __init__(self, status, ticket_number, ticket_creator, staff_id, email, problem):  # Short for initialize
        self.status = status
        self.ticket_number = ticket_number
        self.ticket_creator = ticket_creator
        self.staff_id = staff_id
        self.email = email
        self.problem = problem

    def Issue(self):
        print(self.status+"open")

    def Issued(self):
        print(self.status+"closed")

    def Ticket_Number(self):
        self.ticket_num = random.randint(1000000, 5000000)
