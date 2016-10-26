# Example of a bank account for week 7 exercises. Exercise 2 

class Bank_account:
	
	def __init__(self, name, balance):
		
		self.name = name
		self.balance = balance

	def __str__(self):
		
		return "Customer name: " + self.name + "\nCustomer balance: \xe2\x82\xac" + str(self.balance)

	def lodgement(self):

		deposit = float(raw_input("Lodgement amount: "))
		self.balance = self.balance + deposit
		print "New balance: \xe2\x82\xac" + str(self.balance)
	
	def withdrawal(self):

		withdrawal_amount = float(raw_input("Withdrawal amount: "))
		self.balance = self.balance - withdrawal_amount
		print "New balance: \xe2\x82\xac" + str(self.balance)


if __name__ == "__main__":
	customer = Bank_account("Matthew Swart", 1234.56)
	print customer
	customer.lodgement()
	customer.withdrawal()


