# name: 170. two sum iii data structure design
# link: https://leetcode.com/problems/two-sum-iii-data-structure-design

# solution #
class TwoSum:
	
	def __init__(self):
		self.nums = []
	
	def add(self, number: int) -> None:
		self.nums.append(number)
	
	def find(self, value: int) -> bool:
		if not self.nums:
			return False
		
		# sort the array to use binary search
		self.nums.sort()
		
		left, right = 0, len(self.nums) - 1
		
		while left < right:
			mid = (left + right) // 2
			num = self.nums[left] + self.nums[right]
			
			if num == value:
				return True
			
			if num > value:
				right -= 1
			else:
				left += 1
		
		return False

"""
time complexity:
- add: O(1)
- find: O(n * log(n))

space complexity:
- O(n)
"""