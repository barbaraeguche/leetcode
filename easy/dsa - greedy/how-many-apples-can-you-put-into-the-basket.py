# name: 1196. how many apples can you put into the basket
# link: https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket

# solution #
class Solution:
	def maxNumberOfApples(self, weight: List[int]) -> int:
		weight.sort()
		
		total = 0
		
		for i, w in enumerate(weight):
			total += w
			
			if total > 5000:
				return i
		
		return len(weight)
