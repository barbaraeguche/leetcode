# name: 339. nested list weight sum
# link: https://leetcode.com/problems/nested-list-weight-sum

# solution #
class Solution:
	def depthSum(self, nestedList: List[NestedInteger]) -> int:
		def dfs(nested: List[NestedInteger], depth: int):
			depthSum = 0
			
			for nl in nested:
				if nl.isInteger():
					depthSum += nl.getInteger() * depth
				else:
					depthSum += dfs(nl.getList(), depth + 1)
					
			return depthSum
		
		return dfs(nestedList, 1)

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""