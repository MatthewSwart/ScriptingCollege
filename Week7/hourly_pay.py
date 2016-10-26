#Example of a subclass called hourly pay

from employee import Employee

class Hourly_pay(Employee):

    def __init__(self, staff_name, staff_id, hourly_rate, hours_worked):

        Employee.__init__(self, staff_name, staff_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def total_pay(self):

        return self.hours_worked * self.hourly_rate

    def __str__(self):

        return Employee.__str__(self) + '\nHours worked: ' + str(self.hours_worked) + '\nHourly rate: ' + \
               str(self.hourly_rate) + '\nTotal pay: \xe2\x82\xac' + str(self.total_pay())

def main():

    employee1 = Hourly_pay('Matthew Swart', 1001, 9.95, 21.5)
    print employee1

if __name__ == '__main__':
    main()