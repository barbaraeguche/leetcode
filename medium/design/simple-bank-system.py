# name: 2043. simple bank system
# link: https://leetcode.com/problems/simple-bank-system

# solution #
class Bank:
	
	def __init__(self, balance: List[int]):
		self.balances = balance
	
	def transfer(self, account1: int, account2: int, money: int) -> bool:
		# account needs to exist
		if not (self.validateAccount(account1) and self.validateAccount(account2)):
			return False
		
		# account indices
		account1, account2 = account1 - 1, account2 - 1
		
		# must have sufficient money
		if not self.validateBalance(account1, money):
			return False
		
		# perform transfer
		self.balances[account1] -= money
		self.balances[account2] += money
		
		return True
	
	def deposit(self, account: int, money: int) -> bool:
		if not self.validateAccount(account):
			return False
		
		# account index
		account -= 1
		# perform deposit
		self.balances[account] += money
		
		return True
	
	def withdraw(self, account: int, money: int) -> bool:
		if not self.validateAccount(account):
			return False
		
		# account index
		account -= 1
		
		# must have sufficient money
		if not self.validateBalance(account, money):
			return False
		
		# perform withdrawal
		self.balances[account] -= money
		return True
	
	# make sure the account exists
	def validateAccount(self, account: int) -> bool:
		return 1 <= account <= len(self.balances)
	
	# make sure money in the account is sufficient
	def validateBalance(self, accountIdx: int, money: int) -> bool:
		return money <= self.balances[accountIdx]
