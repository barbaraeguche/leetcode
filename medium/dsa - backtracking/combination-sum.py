# name: 39. combination sum
# link: https://leetcode.com/problems/combination-sum

# solution #
class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		length, combinations = len(candidates), []
		
		def validCombSum(idx: int, target: int, path: List[int]):
			# found a combination sum
			if target == 0:
				combinations.append(path[:])
				return
			
			# invalid combination
			if target < 0:
				return
			
			for i in range(idx, length):
				num = candidates[i]
				# take current num
				path.append(num)
				
				# find all possible combinations
				validCombSum(i, target - num, path)
				# backtrack
				path.pop()
		
		validCombSum(0, target, [])
		return combinations

"""
time complexity:
- O(n^(t/m)); n is the length of candidates, t is the target, m is the minimal number in the array

space complexity:
- O(t/m)
"""