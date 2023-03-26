class Category:
	def __init__(self, category):
		self.category=category
		self.ledger=list()
	
	def __str__(self):
		str_format=f"{self.category}".center(30, "*")+'\n'
		for ledger in self.ledger:
			str_format+=f"{ledger['description'][:23]:23}{ledger['amount']:7.2f}\n"
		str_format+='Total: '+str(self.get_balance())
		return str_format
	def deposit(self, amount, description=''):
		if amount <= 0:
			raise ValueError("the amount must be positive")
		else:
			self.ledger.append({"amount": amount, "description": description});
			
	def withdraw(self, amount, description=''):
		if amount<0:
			raise ValueError("the amount must be poitive")
		if amount==0 or not self.check_funds(amount):
			return False
		elif self.check_funds(amount):
			self.ledger.append({"amount": -amount, "description": description})
			return True
			
	def get_balance(self):
		return sum([val["amount"] for val in self.ledger])
		
	def transfer(self, amount, category_transfer_to):
		if not self.check_funds(amount):
			return False
		if self.check_funds(amount):
			self.withdraw(amount, f"Transfer to {category_transfer_to.category}")
			category_transfer_to.deposit(amount, f"Transfer from {self.category}")
			return True

	def check_funds(self, amount_to_withdraw):
		current_amount=self.get_balance()
		if current_amount-amount_to_withdraw>=0:
			return True
		if current_amount-amount_to_withdraw<0:
			return False 


def create_spend_chart(categories):
	chart='Percentage spent by category\n'
	withdrawn_dict=dict()
	for category in categories:
		withdrawn_total=list()
		withdrawn_total=sum([-val['amount'] for val in category.ledger if val['amount']<0])
		withdrawn_dict[category.category]=withdrawn_total
	total_withdrawn=sum([val for val in withdrawn_dict.values()])
	percent_withdrawn=dict()
	
	for key, val in withdrawn_dict.items():
		percent_withdrawn[key]=val/total_withdrawn*100
	for percent in range(100, -1, -10):
		chart+=f'{percent:3}|'
		for key, value in percent_withdrawn.items():
			chart+='o'.center(3) if value>=percent else ''.rjust(3)
		chart+=' \n'

	line_rep='----------'
	chart+=f'{line_rep}'.rjust(len(line_rep)+4)	

	letter_index=0
	while True:
		line=str()
		for key in percent_withdrawn.keys():
			line+=key[letter_index].ljust(3) if letter_index<len(key) else ''.ljust(3)
		
		letter_index+=1
		if line.strip()=='':
			break
		chart+='\n'
		chart+=''.rjust(5)
		chart+=line
	
	return chart
