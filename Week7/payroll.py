from employee import Employee
from  hourly_pay import Hourly_pay


employees_list = []

employee1 = Employee('Matthew Swart', 1001)
employee2 = Employee('Fiona Duff', 1002)
employees_list.append(employee1)
employees_list.append(employee2)

hourly1 = Hourly_pay('Jordan Harrison', 1003, 9.95, 21.5)
hourly2 = Hourly_pay('Mikola Christodoulo', 1004, 15.50, 112)
employees_list.append(hourly1)
employees_list.append(hourly2)


for staff in employees_list:
    print staff
    print '\n'