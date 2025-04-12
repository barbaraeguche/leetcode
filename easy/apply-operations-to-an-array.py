# name: 2460. apply operations to an array
# link: https://leetcode.com/problems/apply-operations-to-an-array

# solution #
class Solution:
	def applyOperations(self, nums: List[int]) -> List[int]:
		curr = nums[0]
		
		for i, num in enumerate(nums[1:]):
			if curr == num:
				nums[i] = curr * 2
				nums[i+1] = 0
			
			curr = nums[i+1]
		
		# call move zero function
		self.move_zeroes(nums)
		
		return nums
	
	@staticmethod
	def move_zeroes(arr: List[int]) -> None:
		idx = 0
		
		for num in arr:
			if num != 0:
				arr[idx] = num
				idx += 1
		
		while idx < len(arr):
			arr[idx] = 0
			idx += 1