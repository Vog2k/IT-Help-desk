class Employee:

    def __init__(self, first, last, id):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@whitecliffe"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

def main():
    Employee()