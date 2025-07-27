# name: 1299. replace elements with greatest element on right side
# link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side

# solution #
class Solution:
	def replaceElements(self, arr: List[int]) -> List[int]:
		maxRight = -1
		
		for i in range(1, len(arr)):
			# save the current num
			prevNum = arr[-i-1]
			
			# update with next maximum
			arr[-i-1] = max(arr[-i], maxRight)
			# update maximum
			maxRight = max(maxRight, prevNum)
		
		# update the last value
		arr[-1] = -1
		
		return arr
	
"""
time complexity:
- O(n)

space complexity:
- O(1)
"""