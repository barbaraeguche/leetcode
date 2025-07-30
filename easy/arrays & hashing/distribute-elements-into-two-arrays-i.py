# name: 3069. distribute elements into two arrays i
# link: https://leetcode.com/problems/distribute-elements-into-two-arrays-i

# solution #
class Solution:
	def resultArray(self, nums: List[int]) -> List[int]:
		arr1, arr2 = [nums[0]], [nums[1]]
		
		for num in nums[2:]:
			if arr1[-1] > arr2[-1]:
				arr1.append(num)
			else:
				arr2.append(num)
		
		return arr1 + arr2
