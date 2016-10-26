#This is a representation of a employee superclass

class Employee:

    def __init__(self, staff_name, staff_id):

        self.staff_name = staff_name
        self.staff_id = staff_id

    def __str__(self):

        return 'Staff name: ' + self.staff_name + '\nStaff ID: ' + str(self.staff_id)

def main():

    matthew = Employee('Matthew Swart', 1001)
    print matthew

if __name__ == '__main__':

    main()