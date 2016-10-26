x = 0

firstName = input('Enter contacts first name here: ')
lastName = input('Enter contacts surname name here: ')
home = int(input('Enter home number: '))
work = int(input('Enter work number'))

contacts = {'First': firstName, 'Surename' : lastName, 'Home' : home, 'Work' : work}

print (contacts['First'], contacts['Surename'])
print (contacts['Home'])
print (contacts['Work'])

