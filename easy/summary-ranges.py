# name: 228. summary ranges
# link: https://leetcode.com/problems/summary-ranges

# solution #
class Solution:
	def summaryRanges(self, nums: List[int]) -> List[str]:
		if len(nums) == 0:
			return nums
		
		if len(nums) == 1:
			return [str(nums[0])]
		
		arr = []
		curr, string = nums[0], str(nums[0])
		
		for num in nums[1:]:
			if curr == num - 1:
				string += f"#{str(num)}"
			else:
				arr.append(self.format_str(string))
				string = str(num)
			
			curr = num
		
		# append the last string
		arr.append(self.format_str(string))
		
		return arr
	
	@staticmethod
	def format_str(string: str) -> str:
		if '#' not in string:
			return string
		
		splitted = string.split('#')
		return f"{splitted[0]}->{splitted[-1]}"
	