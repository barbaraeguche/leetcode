# name: 1603. design parking system
# link: https://leetcode.com/problems/design-parking-system

# solution #
class ParkingSystem:
	
	def __init__(self, big: int, medium: int, small: int):
		self.big = big
		self.medium = medium
		self.small = small
	
	def addCar(self, carType: int) -> bool:
		if carType == 1:
			self.big -= 1
			return self.big + 1 > 0
		elif carType == 2:
			self.medium -= 1
			return self.medium + 1 > 0
		elif carType == 3:
			self.small -= 1
			return self.small + 1 > 0